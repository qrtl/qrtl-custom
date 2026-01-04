# Product Odoo Module

This addon tracks Odoo modules you maintain as products and registers which customers
subscribe to each module variant with a monthly maintenance fee.

## Usage

1. Create a module product template:

   - Go to Sales > Products > Odoo Modules.
   - Create a product and enable **Is Odoo Module**.
   - Fill in the technical name and repository URL as needed.
   - Tip: module products are typically **Service** products.

2. Create variants by Odoo Series (when needed):

   - On the product template, add an attribute line for **Odoo Series**.
   - Select the required values (14, 15, 16, 17) to generate variants.
   - Variants are created manually by adding the attribute line; the addon does not
     auto-assign it.

3. Register customer subscriptions:
   - Go to Sales > Products > Customer Modules.
   - Create a line with Customer, Module variant, monthly fee, and date range.

Smart buttons:

- **Modules** on a customer shows active module lines for that customer.
- **Customers** on a module template shows active customer lines for its variants.
