# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = "project.task"

    allow_unrelated_followers = fields.Boolean()

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, **kwargs):
        if not self.allow_unrelated_followers:
            explicit_partner_ids = kwargs.get("partner_ids", [])
            # Extract partner IDs from the followers
            follower_partner_ids = [
                follower.partner_id.id for follower in self.message_follower_ids
            ]
            # Combine both lists for validation
            all_recipients = list(set(explicit_partner_ids + follower_partner_ids))
            for partner_id in all_recipients:
                partner = self.env["res.partner"].browse(partner_id)
                if (
                    not partner.user_ids
                    and partner != self.project_id.commercial_partner_id
                ):
                    raise ValidationError(
                        _(
                            "The message recipient should belong"
                            " to the commercial partner of the project."
                        )
                    )
        return super().message_post(**kwargs)
