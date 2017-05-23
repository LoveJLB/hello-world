# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Zhengzhao(models.Model):
    _name = "zhengzhao"
    _description = "证照管理"
    _inherit = ['mail.thread']



    ygxingming = fields.Many2one('hr.employee', string= '员工姓名', default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    # user_id = fields.Many2one('res.users', index=True, track_visibility='onchange',
    #                           default=lambda self: self.env.uid)
    # user_login = fields.Char(related='user_id.login', readonly=True)
    ygbumen = fields.Many2one('hr.department', string='员工部门', related='ygxingming.department_id')
    yggangwei=fields.Char('员工岗位')
    ygbianhao= fields.Char('员工编号')
    shifoutegang =fields.Selection([('yes', '是'), ('no', '否')], '是否为特岗人员')
    yuanjian= fields.Html('原件管理', attachment=True)

    state = fields.Selection(
            [('draft', '证照创建'), ('confirmed', '已提交'), ('done', '审批完成'), ],
            string='状态', default='draft', readonly=True, track_visibility=True)




    def _track_subtype(self, init_values):

        if 'state' in init_values and self.state == 'draft':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'confirmed':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'done':
            return 'mail.mt_comment'
        return False


    @api.multi
    def action_draft(self):
        self.state = 'draft'


    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'


    @api.multi
    def action_done(self):
        self.state = 'done'

    @api.onchange('ygxingming')
    def _onchange_employee(self):
        self.department_id = self.ygxingming.department_id