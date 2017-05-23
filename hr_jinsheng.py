# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Jinsheng(models.Model):
    _name = 'jinsheng'
    _description = '晋升申请表'
    _inherit = ['mail.thread']


    ygxingming = fields.Many2one('hr.employee', '姓名', requird=True, default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    bianhao = fields.Char('编号', related='ygxingming.bianhao', store=True)
    yuanbumen = fields.Many2one('hr.department', '原部门', related='ygxingming.department_id', store=True)
    yuanzhiwei = fields.Many2one('gangwei', related='ygxingming.job_id', string='原岗位')
    ruzhishijian = fields.Date('入职时间', related='ygxingming.shixifrom')
    renzhiqi = fields.Char('任职期')
    jinshenbumen = fields.Many2one('hr.department', '晋升部门')
    jinshengzhiwei = fields.Char('晋升职位')
    gerenongjieyujinshengshenqing = fields.Text('申请总结')
    gerenqianzi = fields.Char('签字')
    gerenqianziriqi = fields.Datetime('日期')
    gongduanzhangyijian = fields.Text('工段长意见')
    gongduanzhangqianzi = fields.Char('签字')
    gongduanzhangqianziriqi = fields.Datetime('日期')
    buzhangyijian = fields.Text('部长意见')
    buzhangqianzi = fields.Char('签字')
    buhangqianziriqi = fields.Datetime('日期')
    fenbufuzong = fields.Text('分管副总意见')
    fenguanfuzongqianzi = fields.Char('签字')
    fenguanfuzongqianziriqi = fields.Datetime('日期')
    zongjingli = fields.Text('总经理意见')
    zongjingliqianzi = fields.Char('签字')
    zongjingliqianziriqi = fields.Datetime('日期')
    renliziyuanbubeizhuguidang = fields.Text('人力资源部备注')
    state = fields.Selection(
            [('draft', '填写申请'), ('confirmed', '工段长审批'), ('confirmedt', '部长审批'), ('confirmedh', '分管副总审批'),
             ('confirmedf', '总经理审批'), ('done', '审核完成'), ],
            string='状态', readonly=True, track_visibility=True, default='draft')



    def _track_subtype(self, init_values):

        if 'state' in init_values and self.state == 'draft':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'confirmed':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'confirmedt':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'confirmedh':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'confirmedf':
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
    def action_confirmt(self):
        self.state = 'confirmedt'


    @api.multi
    def action_confirmh(self):
        self.state = 'confirmedh'


    @api.multi
    def action_confirmf(self):
        self.state = 'confirmedf'


    @api.multi
    def action_done(self):
        self.state = 'done'

    @api.onchange('ygxingming')
    def _onchange_employee(self):
        self.yuanbumen = self.ygxingming.department_id

    @api.onchange('ygxingming')
    def _onchange_employee(self):
        self.bianhao = self.ygxingming.bianhao
        self.yuanzhiwei = self.ygxingming.job_id
        self.ruzhishijian = self.ygxingming.shixifrom