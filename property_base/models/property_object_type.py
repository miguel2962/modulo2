# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PropertyObjectType(models.Model):
    _name = "property.object_type"
    _description = "Property Type"

    name = fields.Char(string="Property", required=True)
    note = fields.Text(string="Notes")
    display_name_format = fields.Text(string="Display Name Format")
    allowed_parent_type_ids = fields.Many2many(
        comodel_name="property.object_type",
        relation="rel_allowed_property_parent_type",
        column1="type_id",
        column2="parent_type_id",
        string="Allowed Parent Types",
    )
    need_parent = fields.Boolean(string="Need Parent")
    occupy_ok = fields.Boolean(string="Can Be Occupied")
    active = fields.Boolean(string="Active", default=True)
    window_action_id = fields.Many2one(comodel_name="ir.actions.act_window", string="Window Action")
    menu_id = fields.Many2one(comodel_name="ir.ui.menu", string="Menu")
    menu_sequence = fields.Integer(string="Menu Sequence", required=True, default=5)

    def action_create_menu(self):
        for document in self:
            window_action = self._create_window_action()
            menu = self._create_menu(window_action)
            document.write({
                "window_action_id": window_action.id,
                "menu_id": menu.id,
            })

    def action_reload(self):
        for document in self:
            document.window_action_id.write(document._prepare_waction_reload())
            document.menu_id.write(document._prepare_menu_reload())

    def _create_window_action(self):
        self.ensure_one()
        obj_waction = self.env["ir.actions.act_window"]
        return obj_waction.create(self._prepare_window_action())

    def _prepare_window_action(self):
        self.ensure_one()
        return {
            "name": self.name,
            "type": "ir.actions.act_window",
            "res_model": "property.object",
            "view_type": "form",
            "view_mode": "tree,form",
            "domain": [("type_id", "=", self.id)],
            "context": {
                "default_type_id": self.id,
                "hide_type": True,
            },
        }

    def _prepare_waction_reload(self):
        self.ensure_one()
        return {
            "name": self.name,
            "domain": [("type_id", "=", self.id)],
            "context": {
                "default_type_id": self.id,
                "hide_type": True,
            },
        }

    def _create_menu(self, window_action):
        self.ensure_one()
        obj_menu = self.env["ir.ui.menu"]
        return obj_menu.create(self._prepare_menu(window_action))

    def _prepare_menu(self, window_action):
        self.ensure_one()
        parent_menu = self.env.ref("property_base.menu_property")
        return {
            "name": self.name,
            "action": f"ir.actions.act_window,{window_action.id}",
            "parent_id": parent_menu.id,
            "sequence": self.menu_sequence,
        }

    def _prepare_menu_reload(self):
        self.ensure_one()
        return {
            "name": self.name,
            "sequence": self.menu_sequence,
        }
