from odoo import api, fields, models


class HelloWorldRecord(models.Model):
    # table name
    _name = 'hello_world_record'
    _description = 'Hello World Record'
    title = fields.Char(string='标题', required=True)
    date = fields.Date(string='创建日期', required=True)
    creator = fields.Char(string='创建者', required=True)
    address = fields.Char(string='地址')
    comments = fields.Text(string='内容')
    where_to_load = fields.Selection([('a', '啊'), ('b', '吧'), ('c', '从')], string='哪里')
