# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Tiaogangshenqing(models.Model):
    _name = 'tiaogang'
    _description = '调岗申请'
    _inherit = ['mail.thread']


    shenqingren = fields.Many2one('hr.employee', '申请人', required=True, default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    shenqingriqi = fields.Date('申请日期')
    yuanbumen = fields.Many2one('hr.department', '原部门', related='shenqingren.department_id', store=True)
    yuangangwei = fields.Many2one('gangwei', '原岗位', related='shenqingren.job_id')
    tiaozhihebumen = fields.Many2one('hr.department', '调至何部门')
    tiaoganghouzhiweimingcheng = fields.Char('调岗后职位名称')
    tiaogangyuanyin = fields.Text('调岗原因')
    shenqingrenqianming = fields.Char('申请人签名')
    shenqingrenqianmingriqi = fields.Date('日期')
    shifoutongyibenrenzhuangang = fields.Boolean('是否同意本人转岗')
    yuanzhishubumengongduanzhangjianyi = fields.Text('原直属部门工段长建议')
    yuanbumengongduanzhangqianzi = fields.Char('签字')
    yuanbumengongduanzhangqianziriqi = fields.Date('日期')
    nizhuangangweibumengongduanzhangyijian = fields.Text('拟转岗位部门工段长意见')
    nizhuangangweigongduanzhangqianzi = fields.Char('签字')
    nizhuangangweigongduanzhangqianziriqi = fields.Date('日期')
    shifoutongyibenrenzhuangang2 = fields.Boolean('是否同意本人转岗')
    yuanzhishubumenbuzhangyijian = fields.Text('原直属部门部长意见')
    yuanzhishubumenbuzhangqianzi = fields.Char('签字')
    yuanzhishubumenbuzhangqianziriqi = fields.Date('日期')
    nizhuangangbumenbuzhangyijian = fields.Text('意见')
    nizhuangangbumenbuzhangqianzi = fields.Char('签字')
    nizhuangangbumenbuzhangqianziriqi = fields.Date('日期')
    shifoutongyizhuangang3 = fields.Boolean('是否同意本人转岗')
    yuangangweifenguanlingdaoyijian = fields.Text('意见')
    yuangangweifenguanlingdaoqianzi = fields.Char('签字')
    yuangangweifenguanlingdaoqianziriqi = fields.Date('日期')
    nizhuangangfenguanlingdaoyijian = fields.Text('意见')
    nizhuangangfenguanlingdaoqianzi = fields.Char('签字')
    nizhuangangfenguanlingdaoqianziriqi = fields.Date('日期')
    renliziyuanbucundang = fields.Text('人力资源部备注')
    state = fields.Selection(
            [('draft', '填写申请'), ('confirmed', '原工段长'), ('confirmedt', '拟转部门工段长'), ('confirmedh', '原部长'),
             ('confirmedf', '拟转部门部长'), ('confirmedi', '原分管领导'), ('confirmeds', '拟转部门分管领导'), ('done', '审核完成'), ],
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
    def action_done(self):
        self.state = 'done'



