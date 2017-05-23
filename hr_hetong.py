# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Hetong(models.Model):
    _name = "hetong"
    _description = "合同管理"
    _inherit = ['mail.thread']



    name = fields.Char(string='合同编号', store=True, required=True)
    htleixing = fields.Char(string='合同类型')
    htqixian = fields.Char(string='合同期限')
    xvdincishu = fields.Integer(string='续订次数')
    ygxingming = fields.Many2one('hr.employee', '员工姓名', required=True)
    ygbumen = fields.Many2one('hr.department', related='ygxingming.department_id', string='员工部门')
    yggangwei = fields.Many2one('gangwei', '员工岗位', related='ygxingming.job_id')
    ygbianhao = fields.Char('员工编号', related='ygxingming.bianhao')
    yuanjian = fields.Binary('原件管理')
    htshuoming = fields.Text('合同说明', help="请填写必要的合同说明")
    state = fields.Selection(
            [('draft', '合同创建'), ('confirmed', '人力资源部部长审批'), ('done', '审批完成'), ],
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
    def _onchangge_ygxingming(self):
        self.ygbumen = self.ygxingming.department_id
        self.yggangwei = self.ygxingming.job_id
        self.ygbianhao = self.ygxingming.bianhao