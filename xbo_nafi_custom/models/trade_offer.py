# -*- coding: utf-8 -*-

from odoo import fields, models


class TradeOffer(models.Model):
    _name = "trade.offer"
    _description = "Trade Offer"

    fixed_per = fields.Float(string='Fixed %')