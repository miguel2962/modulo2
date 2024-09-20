# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class RentalPropertyRecurringFeeSchedule(models.Model):
    _name = "rental.property_recurring_fee_schedule"
    _description = "Property Rental Recurring Fee Schedule"
    _inherit = [
        "rental.recurring_fee_schedule_common",
    ]

    def _compute_rental_state(self):
        super(RentalPropertyRecurringFeeSchedule, self)._compute_rental_state()

    @api.depends("recurring_fee_id.detail_id.rental_id.state")
    def _compute_state(self):
        super(RentalPropertyRecurringFeeSchedule, self)._compute_state()

    recurring_fee_id = fields.Many2one(
        string="Details",
        comodel_name="rental.property_recurring_fee",
    )
    invoice_id = fields.Many2one(
        related="invoice_line_id.invoice_id",
    )
    state = fields.Selection(
        compute="_compute_state",
    )
