# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class RentalPropertyRecurringFee(models.Model):
    _name = "rental.property_recurring_fee"
    _description = "Property Rental Recurring Fee"
    _inherit = [
        "rental.recurring_fee_common",
    ]

    def _compute_rental_state(self):
        super(RentalPropertyRecurringFee, self)._compute_rental_state()

    @api.depends("type_id")
    def _compute_allowed_product(self):
        super(RentalPropertyRecurringFee, self)._compute_allowed_product()

    detail_id = fields.Many2one(
        string="Details",
        comodel_name="rental.property_detail",
    )

    taxes_id = fields.Many2many(
        string="Taxes",
        comodel_name="account.tax",
        relation="rel_rental_property_recurring_fee_taxes",
        column1="property_recurring_fee_id",
        column2="tax_id",
    )

    recurring_fee_schedule_ids = fields.One2many(
        string="Schedule",
        comodel_name="rental.property_recurring_fee_schedule",
        inverse_name="recurring_fee_id",
    )
