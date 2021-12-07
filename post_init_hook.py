from odoo import SUPERUSER_ID, api


def update_database_expire(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["ir.config_parameter"].sudo().set_param(
        "database.expiration_date", "2090-12-31 23:59:59"
    )
