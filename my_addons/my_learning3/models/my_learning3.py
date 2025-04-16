from odoo import api, fields, models


class MyLearning3(models.Model):
    _name = 'my_learning3'
    name = fields.Char(string='Name', required=True)
    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    radio1 = fields.Selection(selection=[('a', '1'), ('b', '2'), ('c', '3')], string='Choice 1', required=True)
