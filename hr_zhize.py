# -*- coding: utf-8 -*-
from odoo import fields, models

class Zhize(models.Model):
    _name = 'zhize'
    _description = u'职责'


    name = fields.Char('序号')
    neirong = fields.Text('内容')
    shejiguocheng = fields.Char('涉及过程')
    guochengbianhao = fields.Char('过程编号')
    gangwei = fields.One2many('gangwei', 'zhizeliebiao')
    state = fields.Selection([('draft', '草稿'), ('confirmed', '实施')], string='状态', defalut='draft')