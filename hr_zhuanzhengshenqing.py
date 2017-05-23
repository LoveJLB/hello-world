# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Zhuanzhengshenqing(models.Model):
    _name = 'zhuanzhengshenqing'
    _description = '转正申请'
    _inherit = ['mail.thread']


    ygxingming = fields.Many2one('hr.employee', '员工姓名', required=True, default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    ygbianhao = fields.Char('员工编号', required=True, related='ygxingming.bianhao', store=True)
    ygbumen = fields.Many2one('hr.department', '所属部门', required=True, related='ygxingming.department_id')
    yggangwei = fields.Many2one('gangwei', '员工岗位', related='ygxingming.job_id')
    xingbie = fields.Selection([('male', '男'), ('female', '女')], '性别')
    zuigaoxueli= fields.Selection(
            [('boshi', '博士'), ('shuoshi', '硕士'), ('benke', '本科'), ('gaozhongjiyixia', '高中及以下')], string='最高学历')
    ruzhishijian = fields.Date('入职时间', related='ygxingming.shixifrom')
    ziwojianding = fields.Text('自我鉴定')
    shangjipingjia = fields.Text('上级评价')
    buzhangshenhe = fields.Text('部长审核')
    lingdaoshenhe = fields.Text('分管领导审核')
    rlzybsh = fields.Text('人力资源部审核')
    benrenqianzi = fields.Char('本人签字')
    shangjiqianzi = fields.Char('签字')
    buzhangqianzi = fields.Char('签字')
    lingdaoqianzi = fields.Char('签字')
    rlzyqz = fields.Char('签字')
    riqi1 = fields.Date('日期')
    riqier = fields.Date('日期')
    riqisan = fields.Date('日期')
    riqisi = fields.Date('日期')
    riqiwu = fields.Date('日期')
    kaoheyijian = fields.Selection([('tiqianzhuanzheng', '提前转正'), ('anqizhuanzheng', '按期转正'), ('yanqizhuanzheng', '延期转正')], '考核意见')
    kaoheyijianer = fields.Selection(
            [('tiqianzhuanzheng', '提前转正'), ('anqizhuanzheng', '按期转正'), ('yanqizhuanzheng', '延期转正')], '考核意见')
    kaoheyijiansan = fields.Selection(
            [('tiqianzhuanzheng', '提前转正'), ('anqizhuanzheng', '按期转正'), ('yanqizhuanzheng', '延期转正')], '考核意见')
    kaoheyijiansi = fields.Selection(
            [('tiqianzhuanzheng', '提前转正'), ('anqizhuanzheng', '按期转正'), ('yanqizhuanzheng', '延期转正')], '考核意见')
    state = fields.Selection(
            [('draft', '个人自我鉴定'), ('confirmed', '直接上级评价'), ('confirmedt', '部长审核'), ('confirmedh', '分管领导审核'), ('confirmedf', '人力资源部审核'),
             ('done', '审核完成'), ],
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
        self.ygbumen = self.ygxingming.department_id

    @api.onchange('ygxingming')
    def _onchange_employee(self):
        self.ygbianhao = self.ygxingming.bianhao
        self.yggangwei = self.ygxingming.job_id
        self.ruzhishijian = self.ygxingming.shixifrom