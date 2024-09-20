# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PropertyObject(models.Model):
    _name = "property.object"
    _description = "Common Class for Property Object"

    @api.depends("type_id")
    def _compute_allowed_parent_type_ids(self):
        for document in self:
            document.allowed_parent_type_ids = document.type_id.allowed_parent_type_ids.ids if document.type_id else []

    @api.depends("type_id", "parent_id")
    def _compute_full_name(self):
        for document in self:
            address_format = document.type_id.display_name_format or "%(name)s"
            args = {
                "name": document.name,
                "parent_name": document.parent_id.full_name if document.parent_id else '',
                "parent_full_name": document.parent_id.full_name if document.parent_id else '',
            }
            document.full_name = address_format % args

    @api.depends("type_id")
    def _compute_need_parent(self):
        for document in self:
            document.need_parent = document.type_id.need_parent if document.type_id else False

    @api.depends("type_id")
    def _compute_occupy_ok(self):
        for document in self:
            document.occupy_ok = document.type_id.occupy_ok if document.type_id else False

    name = fields.Char(
        string="Property",
        required=True,
    )
    full_name = fields.Char(
        string="Full Name",
        compute="_compute_full_name",
        store=False,
    )
    note = fields.Text(string="Notes")
    active = fields.Boolean(default=True, string="Active")
    parent_id = fields.Many2one(comodel_name="property.object", string="Parent Property")
    occupy_ok = fields.Boolean(compute="_compute_occupy_ok", store=False, string="Can Be Occupied")
    need_parent = fields.Boolean(compute="_compute_need_parent", store=False, string="Need Parent")
    child_ids = fields.One2many(comodel_name="property.object", inverse_name="parent_id", string="Child Properties")
    allowed_parent_type_ids = fields.Many2many(comodel_name="property.object_type", compute="_compute_allowed_parent_type_ids", store=False, string="Allowed Parent Types")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Owner")
    type_id = fields.Many2one(comodel_name="property.object_type", string="Type")
    size = fields.Float(string="Property Size")
    size_uom_id = fields.Many2one(comodel_name="product.uom", string="UoM")
    owner_id = fields.Many2one(comodel_name="res.partner", domain="[('parent_id', '=', False)]", string="Owner")
    tenant_id = fields.Many2one(comodel_name="res.partner", domain="[('parent_id', '=', False)]", string="Occupant")
    tenancy_status_id = fields.Many2one(comodel_name="property.tenacy_status", string="Occupancy Status")
    availability_status_id = fields.Many2one(comodel_name="property.availability_status", string="Availability Status")
    product_id = fields.Many2one(comodel_name="product.product", string="Product Link")

    @api.onchange("type_id")
    def onchange_parent_id(self):
        self.parent_id = False

    def name_get(self):
        return [(document.id, document.full_name) for document in self]
