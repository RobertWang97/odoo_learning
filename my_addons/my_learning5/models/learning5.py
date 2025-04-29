from odoo import api, fields, models


class learning5(models.Model):

    def _default_current_user_id(self):
        return self.env.user.id

    _name = 'learning5'
    _description = 'Learning 5'
    name2 = fields.Char(string='姓名', required=True)
    comment2 = fields.Text(string='备注')
    selection2 = fields.Selection([('1', '111'), ('2', '222'), ('3', '333')],
                                  default='2', string='哪里')
    many2one2 = fields.Many2one('res.users',
                                string='填报人',
                                default=lambda self: self.env.uid, required=True)
    id2 = fields.Many2one('res.users',
                          string='填报人2',
                          default=_default_current_user_id, required=True)
