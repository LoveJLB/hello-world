# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Renli(models.Model):
    _name = 'renlixuqiu'
    _description = '人员需求确认单'
    _inherit = ['mail.thread']


    zhiwei= fields.Many2one('gangwei', '职位', required=True)
    renshu= fields.Integer('人数')
    riqi= fields.Datetime('填表日期')
    zhijieshangji= fields.Many2one('hr.employee', '直属上级')
    xiwangdaogangshijian= fields.Datetime('希望到岗时间')
    xingbie= fields.Char('性别')
    nianliang= fields.Integer('年龄')
    xueli= fields.Char('学历')
    zhuanyeyaoqiu= fields.Char('专业要求')
    changbaiban= fields.Boolean('长白班')
    sanbaban= fields.Boolean('三八班')
    shierershisi= fields.Boolean('上12休24')
    shiershier= fields.Boolean('上12休12')
    changbaibanjiaban= fields.Boolean('长白班加班')
    gangweizhize= fields.Text('岗位职责')
    zuijiaxuanze= fields.Text('最佳选择')
    yingxingtiaojian= fields.Text('硬性条件')
    ruanxingtiaojian= fields.Text('软性条件')
    bumen= fields.Many2one('hr.department', '部门')
    bumenrenyuan= fields.Many2many('hr.employee')
    shenqingrenqianzi= fields.Char('申请人签字')
    shenqingbumenbuzhangqianzi= fields.Char('申请部门部长签字')
    fenguanfuzongshenpi= fields.Text('分管副总审批')
    zongjinglishenpi= fields.Text('总经理审批')
    renliziyuanshenpi= fields.Text('人力资源部存档')
    jihuabiandongxiangmu= fields.Text('计划变动项目')
    state = fields.Selection(
            [('draft', '建立人员需求单'), ('confirmed', '分管副总审批'), ('confirmedt', '总经理审批'), ('confirmedh', '人力资源部存档'),
             # ('confirmedf', '后勤部审批'), ('confirmedi', '财务部审批'), ('confirmeds', '分管领导审批'), ('confirmede', '人力资源部审批'),
             ('done', '审核完成')],
            string='状态', readonly=True, track_visibility=True, default='draft')



    def _track_subtype(self,init_values):

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