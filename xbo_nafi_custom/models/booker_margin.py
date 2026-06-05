# -*- coding: utf-8 -*-

from odoo import fields, models


class BookerMargin(models.Model):
    _name = "booker.margin"
    _description = "Booker Margin"

    fixed_per = fields.Float(string='Fixed %')