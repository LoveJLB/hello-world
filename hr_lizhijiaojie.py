# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Lizhijiaojie(models.Model):
    _name = 'lizhijiaojie'
    _description = '离职交接单'
    _inherit = ['mail.thread']


    lizhirenxingming = fields.Many2one('hr.employee', '离职人姓名', required=True,  default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    yuangongbianhao = fields.Char(' 编号', store=True, related='lizhirenxingming.bianhao')
    yuanbumeng = fields.Many2one('hr.department', '原部门', store=True, related='lizhirenxingming.department_id')
    yuangangwei = fields.Many2one('gangwei', string='原岗位', related='lizhirenxingming.job_id')
    lizhishijian = fields.Datetime('离职时间')
    gongzuojiaojie = fields.Boolean('工作交接')
    yiqideng = fields.Boolean('电脑、仪器、工具')
    bangongyaoshi = fields.Boolean('办公钥匙')
    gongduanzhangqianzi = fields.Char('签字')
    gongduanzhangqianziriqi = fields.Datetime('日期')
    Upan = fields.Boolean('U盘')
    caigoubuqianzi = fields.Char('签字')
    caigoubuqianziriqi = fields.Datetime('日期')
    suoshubumenbuzhang = fields.Text('所属部门部长')
    buzhangqianzi = fields.Char('部长签字')
    buzhangqianziriqi = fields.Datetime('日期')
    houqingbu = fields.Text('后勤部')
    houqinbuqianzi = fields.Char('后勤部签字')
    houqinbuqianziriqi = fields.Datetime('日期')
    caiwubu = fields.Text('财务部')
    caiwubuqianzi = fields.Char('签字')
    caiwubuqianziriqi = fields.Datetime('日期')
    fenguanlingdao = fields.Text('分管领导')
    fenguanlingdaoqianzi = fields.Char('签字')
    fenguanlingdaoqianziriqi = fields.Datetime('日期')
    tongxungongju = fields.Boolean('对讲机')
    gongzhuang = fields.Boolean('工装、工帽、工鞋')
    fanka = fields.Boolean('饭卡、工牌、鞋柜钥匙')
    laodonghetong = fields.Boolean('劳动合同')
    jiechuzhongzhilaodonghetongzhengmingsu = fields.Boolean('接触终止劳动合同证明书')
    qita = fields.Text('其它')
    beizhu = fields.Text('备注')
    state = fields.Selection(
            [('draft', '填写离职申请表'), ('confirmed', '工段长审批'), ('confirmedt', '采购部审批'), ('confirmedh', '部长审批'), ('confirmedf', '后勤部审批'), ('confirmedi', '财务部审批'), ('confirmeds', '分管领导审批'), ('confirmede', '人力资源部审批'), ('done', '审核完成')],
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
        if 'state' in init_values and self.state == 'confirmedi':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'confirmeds':
            return 'mail.mt_comment'
        if 'state' in init_values and self.state == 'confirmede':
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
    def action_confirmi(self):
        self.state = 'confirmedi'

    @api.multi
    def action_confirms(self):
        self.state = 'confirmeds'

    @api.multi
    def action_confirme(self):
        self.state = 'confirmede'

    @api.multi
    def action_done(self):
        self.state = 'done'

    @api.onchange('lizhirenxingming')
    def _onchange_employee(self):
        self.yuanbumeng = self.lizhirenxingming.department_id

    @api.onchange('lizhirenxingming')
    def _onchange_bianhao(self):
        self.yuangongbianhao = self.lizhirenxingming.bianhao