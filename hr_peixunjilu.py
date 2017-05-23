# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Peixun(models.Model):
    _name = 'peixun'
    _description = u'培训'


    peixunshijian = fields.Datetime('培训时间')
    peixunbumen = fields.Many2one('hr.department', '培训部门')
    peixundidian = fields.Char('培训地点')
    peixunjiangshi = fields.Char('培训讲师')
    peixunzhuti = fields.Char('培训主题')
    canjiapeixunrenyuan = fields.Text('参加培训人员', help="手写签到")
    peixunmudi = fields.Text('培训目的')
    peixunneirongzhaiyao = fields.Text('培训内容摘要')
    peixunkaohejieguo = fields.Text('培训考核结果')
    peixunxiaoguopingjia = fields.Text('培训效果评价', help="人力资源部填写")
    beizhu = fields.Text('备注')
    state = fields.Selection([('nostart', '未开始培训'), ('done', '培训结束')], string='培训状态', default='nostart')
