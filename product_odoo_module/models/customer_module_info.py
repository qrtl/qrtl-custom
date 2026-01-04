# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class CustomerModuleInfo(models.Model):
    _name = "customer.module.info"
    _description = "Customer Module Information"
    _order = "partner_id, product_id, date_start desc"

    name = fields.Char(compute="_compute_name")
    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        ondelete="cascade",
    )
    product_id = fields.Many2one(
        "product.product",
        domain=[("is_odoo_module", "=", True)],
        required=True,
        ondelete="restrict",
    )
    product_tmpl_id = fields.Many2one(
        related="product_id.product_tmpl_id",
        store=True,
    )
    source_type_id = fields.Many2one(
        related="product_id.source_type_id",
        store=True,
    )
    module_license_id = fields.Many2one(
        related="product_id.module_license_id",
        store=True,
    )
    module_complexity_id = fields.Many2one(
        related="product_id.module_complexity_id",
        store=True,
    )
    customer_count = fields.Integer(
        related="product_tmpl_id.customer_module_count",
        string="Total Customers",
    )
    fee_factor = fields.Float(
        default=1.0,
        help="Multiplier applied to the product's suggested fee.",
    )
    suggested_fee = fields.Monetary(
        compute="_compute_suggested_fee",
        currency_field="currency_id",
    )
    loc = fields.Integer(
        string="Lines of Code",
        related="product_id.loc",
        store=True,
        readonly=True,
    )
    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        related="company_id.currency_id",
        store=True,
        readonly=True,
    )
    monthly_fee = fields.Monetary(required=True)
    date_start = fields.Date(default=fields.Date.context_today)
    date_end = fields.Date()
    active = fields.Boolean(default=True)
    note = fields.Text()
    business_impact_id = fields.Many2one(
        "module.business.impact",
        compute="_compute_business_impact_id",
        store=True,
    )
    series_value_id = fields.Many2one(
        "product.attribute.value",
        compute="_compute_series_value_id",
        store=True,
    )

    @api.depends("product_id", "partner_id")
    def _compute_name(self):
        for record in self:
            record.name = f"{record.product_id.name} - {record.partner_id.ref}"

    @api.depends("product_id", "product_id.business_impact_id")
    def _compute_business_impact_id(self):
        for record in self:
            record.business_impact_id = record.product_id.business_impact_id

    @api.depends("product_id.suggested_fee", "fee_factor")
    def _compute_suggested_fee(self):
        for record in self:
            record.suggested_fee = record.product_id.suggested_fee * record.fee_factor

    @api.depends(
        "product_id",
        "product_id.product_template_attribute_value_ids",
        "product_id.product_template_attribute_value_ids.attribute_id",
    )
    def _compute_series_value_id(self):
        for rec in self:
            rec.series_value_id = False
            if rec.product_id:
                ptavs = rec.product_id.product_template_attribute_value_ids.filtered(
                    lambda v: v.attribute_id.is_odoo_series
                )
                if ptavs:
                    rec.series_value_id = ptavs[0].product_attribute_value_id

    @api.constrains(
        "partner_id",
        "product_id",
        "date_start",
        "date_end",
        "active",
    )
    def _check_date_overlap(self):
        for record in self.filtered("active"):
            if (
                record.date_start
                and record.date_end
                and record.date_end < record.date_start
            ):
                raise ValidationError(
                    _("End date cannot be earlier than the start date.")
                )
            if not record.partner_id or not record.product_id or not record.date_start:
                continue
            domain = [
                ("id", "!=", record.id),
                ("active", "=", True),
                ("partner_id", "=", record.partner_id.id),
                ("product_id", "=", record.product_id.id),
                "|",
                ("date_end", "=", False),
                ("date_end", ">=", record.date_start),
            ]
            if record.date_end:
                domain += [
                    "|",
                    ("date_start", "=", False),
                    ("date_start", "<=", record.date_end),
                ]
            overlap = self.search_count(domain)
            if overlap:
                raise ValidationError(
                    _(
                        "An active customer module already exists for this customer "
                        "and module in the selected period."
                    )
                )
