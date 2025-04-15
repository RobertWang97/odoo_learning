from odoo import api, fields, models


class Learning1(models.Model):
    _name = 'learning1'
    _description = 'Learning'
    name = fields.Char(string='姓名', required=True)
    comment = fields.Text(string='备注')
