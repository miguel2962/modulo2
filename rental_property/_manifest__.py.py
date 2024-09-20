# -*- coding: utf-8 -*-
# Copyright 2024 Florian Solutions
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Rental Property",
    "version": "16.0.1.0.0",
    "category": "Real Estate",
    "summary": "Module to manage rental properties",
    "description": """
        Module to manage rental properties, including scheduling, property details, and configurations.
        This module provides functionalities for managing rental property transactions.
    """,
    "website": "",
    "author": "Florian Solutions",
    "license": "AGPL-3",
    "installable": True,  # Puede quedarse igual
    "application": True,  # Reemplaza a "installable" en algunos casos, pero ambos pueden coexistir
    "depends": [
        "rental_common",  # Verificar si sigue existiendo en la v16 o si ha sido reemplazado
        "property_base"   # Igual que arriba
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/rental_property_type_data.xml",
        "data/base_workflow_policy_data.xml",
        "data/base_cancel_reason_configurator_data.xml",
        "data/ir_cron_data.xml",
        "menu.xml",
        "views/rental_property_views.xml",
        "views/rental_property_detail_views.xml",
        "views/rental_property_detail_schedule_views.xml",
        "views/property_object_views.xml",
    ],
    "demo": [],
    "maintainers": ["Florian Solutions"],  # Se puede añadir para indicar quién mantiene el módulo
    "installable": True,  # Sigue siendo necesario, aunque ahora también puede usarse application
    "auto_install": False,  # Asegura que no se instale automáticamente como dependencia de otro módulo
}
