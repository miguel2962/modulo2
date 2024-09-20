# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class RentalPropertyUpfrontCost(models.Model):
    _name = "rental.property_upfront_cost"
    _description = "Property Rental Upfront Cost"
    _inherit = [
        "rental.upfront_cost_common",
    ]

    @api.depends("type_id")
    def _compute_allowed_product(self):
        super(RentalPropertyUpfrontCost, self)._compute_allowed_product()

    rental_id = fields.Many2one(
        comodel_name="rental.property",
    )
    
    tax_ids = fields.Many2many(
        comodel_name="account.tax",
        relation="rel_rental_property_upfront_cost_tax",
        column1="rental_property_upfront_cost_id",
        column2="tax_id",
    )
