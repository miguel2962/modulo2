from odoo import models


class PropertyObject(models.Model):
    _name = "property.object"
    _inherit = [
        "rental.object",
        "property.object",
    ]