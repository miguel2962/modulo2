# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class PropertyTenancyStatus(models.Model):
    _name = "property.tenancy_status"
    _description = "Tenancy Status"

    name = fields.Char(
        string="Tenancy Status",
        required=True,
    )
    note = fields.Text(
        string="Notes"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
