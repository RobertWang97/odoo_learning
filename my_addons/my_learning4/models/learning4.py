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

    active = fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, vals):
        res = super(learning4, self).create(vals)
        # res.name2 = "ddd"
        return res

    # @api.multi
    @api.model
    def write(self, vals):
        old_value_name = self.name2
        res = super(learning4, self).write(vals)
        new_value_name = self.name2
        return res

    @api.onchange('comment2')
    def onchange_comment2(self):
        self.comment2 = "323"

    # @api.model
    # def unlink(self):
    #     res = super(learning4, self).unlink()
    #     return res

    def unlink(self):
        for obj in self:
            obj.active = False
        return True

    def my_unlink(self):
        self.active = False
        # return super(learning4, self).
        # return True

    def my_search(self):
        domain = [('active', '=', True), ('name2', '=', 'aa')]
        objs = self.search(domain)
        objs2 = self.browse([14, 15])
        print(objs, objs2)
        user_objs = self.env['res.users'].search([('id', '=', 2)])
        user_objs2 = self.env['res.users'].browse([1, 2, 3])
        print(user_objs)
        print(user_objs2)
        user_objs3 = self.env['res.users'].sudo().search([('id', '=', 2)])
        user_objs4 = self.env['res.users'].sudo().browse([1, 2, 3])
        print(user_objs3)
        print(user_objs4)

    def create_or_write(self):
        # self.env['res.users'].create([{
        #     "name": "测试账户",
        #     "email": "aa@dd.com",
        #     "login": "aa@dd.com",
        # }])
        users_env = self.env['res.users'].sudo()
        user_id = users_env.search([("name", "=", "测试账户")])
        res = user_id.write({
            "login": "bb@dd.com"
        })
        return res
