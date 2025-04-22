from odoo import api, fields, models


class learning4(models.Model):
    def _default_current_user_id(self):
        return self.env.user.id

    _name = 'learning4'
    _description = 'Learning 4'
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

    @api.model_create_multi
    def create(self, vals):
        res = super(learning4, self).create(vals)
        res.name2 = "ddd"
        return res

    # @api.multi
    @api.model
    def write(self, vals) :
        res = super(learning4, self).write(vals)
        return res

    @api.onchange('comment2')
    def onchange_comment2(self):
        self.comment2 = "323"
