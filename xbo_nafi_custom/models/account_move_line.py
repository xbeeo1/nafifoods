# -*- coding: utf-8 -*-

from odoo import fields, models,api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'


    trade_price = fields.Float(string="Trade Price")

    dist_margin = fields.Float(
        string="Dist Margin",
        compute="_compute_all_margins_and_price",
        store=True
    )

    booker_margin = fields.Float(
        string="Booker Margin",
        compute="_compute_all_margins_and_price",
        store=True
    )

    trade_Offer = fields.Float(
        string="Trade Offer",
        compute="_compute_all_margins_and_price",
        store=True
    )
    # ----------------------------
    # Product onchange (safe)
    # ----------------------------
    @api.onchange('product_id')
    def onchange_product_id(self):
        for line in self:
            if line.move_id.move_type == 'out_invoice':
                line.trade_price = line.product_id.list_price or 0.0

    @api.depends('trade_price')
    def _compute_all_margins_and_price(self):

        dist_obj = self.env['distributor.margin'].search([], limit=1)
        book_obj = self.env['booker.margin'].search([], limit=1)
        trade_obj = self.env['trade.offer'].search([], limit=1)

        for line in self:
            if line.move_id.move_type != 'out_invoice':
                line.dist_margin = 0.0
                line.booker_margin = 0.0
                line.trade_Offer = 0.0
                continue
            trade_price = line.trade_price or 0.0

            # ---------------- Dist Margin ----------------
            if dist_obj and dist_obj.fixed_per and trade_price and not line.product_id.is_charges:
                dis_dist = trade_price * (dist_obj.fixed_per / 100)
                line.dist_margin = trade_price - dis_dist
            else:
                line.dist_margin = 0.0  # fallback safe value

            # ---------------- Booker Margin ----------------
            if book_obj and book_obj.fixed_per and line.dist_margin and not line.product_id.is_charges:
                dis_book = line.dist_margin * (book_obj.fixed_per / 100)
                line.booker_margin = line.dist_margin - dis_book
            else:
                line.booker_margin = 0.0

            # ---------------- Trade Offer ----------------
            if trade_obj and trade_obj.fixed_per and line.booker_margin and not line.product_id.is_charges:
                discount = line.booker_margin * (trade_obj.fixed_per / 100)
                line.trade_Offer = line.booker_margin - discount
            else:
                line.trade_Offer = 0.0

            # ---------------- Final Price ----------------
            if line.trade_Offer:
                line.price_unit = line.trade_Offer
            elif line.booker_margin:
                line.price_unit = line.booker_margin
            elif line.dist_margin:
                line.price_unit = line.dist_margin
            else:
                line.price_unit = trade_price
