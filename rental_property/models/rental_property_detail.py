# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class RentalPropertyDetail(models.Model):
    _name = "rental.property_detail"
    _description = "Property Rental Detail"
    _inherit = [
        "rental.detail_common",
    ]

    currency_id = fields.Many2one(
        related="rental_id.currency_id",
        store=True,
    )
    year_period = fields.Integer(
        related="rental_id.year_period",
        store=True,
    )
    month_period = fields.Integer(
        related="rental_id.month_period",
        store=True,
    )
    day_period = fields.Integer(
        related="rental_id.day_period",
        store=True,
    )
    hour_period = fields.Integer(
        related="rental_id.hour_period",
        store=True,
    )
    rental_date_start = fields.Datetime(
        related="rental_id.date_start",
        store=True,
    )
    rental_date_end = fields.Datetime(
        related="rental_id.date_end",
        store=True,
    )
    company_id = fields.Many2one(
        related="rental_id.company_id",
    )

    rental_id = fields.Many2one(
        comodel_name="rental.property",
        required=True,
        ondelete="cascade",
    )

    object_id = fields.Many2one(
        string="Property",
        comodel_name="property.object",
        required=True,
    )

    schedule_ids = fields.One2many(
        string="Schedule",
        comodel_name="rental.property_detail_schedule",
        inverse_name="detail_id",
    )

    recurring_fee_ids = fields.One2many(
        string="Recurring Fees",
        comodel_name="rental.property_recurring_fee",
        inverse_name="detail_id",
    )

    taxes_id = fields.Many2many(
        string="Taxes",
        comodel_name="account.tax",
        relation="rel_rental_property_detail_taxes",
        column1="property_detail_id",
        column2="tax_id"
    )

    partner_id = fields.Many2one(
        string="Partner",
        related="rental_id.partner_id",
        readonly=True,
        store=True,
    )
    payment_term_id = fields.Many2one(
        string="Payment Terms",
        related="rental_id.payment_term_id",
        readonly=True,
        store=True,
    )
