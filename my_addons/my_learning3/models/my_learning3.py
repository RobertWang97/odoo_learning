from odoo import api, fields, models


class MyLearning3(models.Model):
    _name = 'my_learning3'
    _description = 'learning 3'
    name = fields.Char(string='Name', required=True)
    title = fields.Char(string='Title')
    description = fields.Text(string='Description')
    radio1 = fields.Selection(selection=[('a', '1'), ('b', '2'), ('c', '3')], string='Choice 1', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    #optional attribute: currency_field='currency_id'
    value = fields.Monetary(string='total')
