from odoo import fields, models, api


class GCUser(models.Model):
    _inherit = "gc.user"

    guilded_uuid = fields.Char()

