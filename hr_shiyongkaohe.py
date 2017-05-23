# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Shiyongkaohe(models.Model):
    _name = "shiyongkaohe"
    _description = "使用考核表"
    _inherit = ['mail.thread']


    ygxingming = fields.Many2one('hr.employee', string='员工姓名', required=True,  default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    ygbianhao = fields.Char('员工编号', required=True, related='ygxingming.bianhao', store=True)
    ygbumen = fields.Many2one('hr.department', '所属部门', required=True, related='ygxingming.department_id')
    shixi_from = fields.Date('实习时间从', required=True, related='ygxingming.shixifrom')
    shixi_to = fields.Date('实习时间到', required=True, related='ygxingming.shixito')
    yggangwei = fields.Many2one('gangwei', string='员工岗位', related='ygxingming.job_id')
    zhouzongjie = fields.Text('周总结')
    one = fields.Text('第一天')
    two = fields.Text('第二天')
    three = fields.Text('第三天')
    four = fields.Text('第四天')
    five = fields.Text('第五天')
    six = fields.Text('第六天')
    seven = fields.Text('第七天')
    zerenxin = fields.Selection([('you', '优'), ('liang', '良'), ('zhong', '中'), ('cha', '差')],'责任心')
    jiluxing = fields.Selection([('you', '优'), ('liang', '良'), ('zhong', '中'), ('cha', '差')], '纪律性')
    jieshounengli = fields.Selection([('you', '优'), ('liang', '良'), ('zhong', '中'), ('cha', '差')], '学习接受能力')
    gongzuozhiliang = fields.Selection([('you', '优'), ('liang', '良'), ('zhong', '中'), ('cha', '差')], '工作质量')
    xiezuoxing = fields.Selection([('you', '优'), ('liang', '良'), ('zhong', '中'), ('cha', '差')], '协作性')
    jijixing = fields.Selection([('you', '优'), ('liang', '良'), ('zhong', '中'), ('cha', '差')], '积极性')
    zongping = fields.Text('总评')
    gongduanzhangqianzi = fields.Char('工段长签字')
    qianziriqi = fields.Datetime('日期')
    buzhangyijianshuoming = fields.Text('部长意见说明')
    buzhangyijian = fields.Selection([('jianyishiyong', '建议试用'), ('zhongzhishiyong', '终止试用')], '部长意见')
    buzhangqianzi = fields.Char('部长签字')
    renliziyuanbuyijianshuoming = fields.Text('人力资源部意见说明')
    renliziyuanbuyijian = fields.Selection([('jianyishiyong', '建议试用'), ('zhongzhishiyong', '终止试用')], '人力资源部意见')
    shuoming = fields.Text('备注')
    state = fields.Selection(
            [('draft', '个人总结'), ('confirmed', '指导人评价'), ('confirmedt', '部长意见'), ('confirmedh', '人力资源部意见'), ('done', '审核完成'), ],
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
    def action_done(self):
        self.state = 'done'

    @api.onchange('ygxingming')
    def _onchange_employee(self):
        self.ygbumen = self.ygxingming.department_id

    @api.onchange('ygxingming')
    def _onchange_bianhao(self):
        self.ygbianhao = self.ygxingming.bianhao
        self.shixi_from = self.ygxingming.shixifrom
        self.shixi_to = self.ygxingming.shixito
        self.yggangwei = self.ygxingming.job_id
