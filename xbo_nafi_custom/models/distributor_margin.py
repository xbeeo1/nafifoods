# -*- coding: utf-8 -*-

from odoo import fields, models


class DistributorMargin(models.Model):
    _name = "distributor.margin"
    _description = "Distributor Margin"

    fixed_per = fields.Float(string='Fixed %')