from odoo import models, fields, api, _


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    def name_get(self):
        return [(wo.id, f'''{wo.product_id}''') for wo in self]
