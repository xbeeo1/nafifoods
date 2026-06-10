# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductVariantInherit(models.Model):
    _inherit = 'product.product'

    is_charges = fields.Boolean(string="Is Charges",related='product_tmpl_id.is_charges', store=True)
