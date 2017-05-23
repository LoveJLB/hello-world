# -*- coding: utf-8 -*-

from odoo import fields, models
class Gangwei(models.Model):
    _name = 'gangwei'
    _description = '岗位管理'

    name = fields.Char('职位名称', required=True, store=True)
    dingbian = fields.Char('定编')
    guishubumen = fields.Many2one('hr.department', string='归属部门')
    zhiweibianma = fields.Char('归属编码')
    zhiweijibie = fields.Char('职位级别')
    zhijieshangji = fields.Char('直接上级')
    zhijiexiaji = fields.Char('直接下级')
    guanlilei = fields.Boolean('管理类')
    zhuanyelei = fields.Boolean('专业类')
    xingzhenglei = fields.Boolean('行政类')
    caozuolei = fields.Boolean('操作类')
    zhanlueguanli = fields.Boolean('战略管理')
    caiwuguanli = fields.Boolean('财务管理')
    renliziyua = fields.Boolean('人力资源')
    jishukaifa = fields.Boolean('技术开发')
    shichangyingxiao = fields.Boolean('市场营销')
    shengchanzhizao = fields.Boolean('生产制造')
    zhiliangguanli = fields.Boolean('质量管理')
    xinxiguanli = fields.Boolean('信息管理')
    xingzhengzhichi = fields.Boolean('行政支持')
    gongyinlian = fields.Boolean('供应链')
    zhiweishezhimudi = fields.Text('职位设置目的')
    gongsineibu = fields.Text('公司内部')
    gongsiwaibu = fields.Text('公司外部')
    jinshenfangxiang = fields.Text('晋升方向')
    lungangfanwei = fields.Text('轮岗范围')
    zhizeliebiao = fields.Many2many('zhize')
    jiaoyuyaoqiu = fields.Selection([('gaozhong', '高中'), ('dazhuan', '大专'), ('benke', '本科及以上'), ('shuohi', '硕士及以上'), ('boshi', '博士')], string='学历')
    zhuanye = fields.Char('专业')
    lilunzhishi = fields.Text('理论知识')
    zhuanyejineng = fields.Text('专业技能')
    hangyejinyan = fields.Text('行业经验要求')
    gongsijinyanyaoqiu = fields.Text('公司经验要求')
    chuchaiqingkuang = fields.Selection([('jinchang', '经常出差'), ('jiaoshao', '较少'), ('wu', '无'), ('qita', '其他')], string='出差情况')
    zhuwai = fields.Selection([('shi', '是'), ('fou', '否')], string='驻外')
    gongzuochangsuo = fields.Selection([('bangonglou', '办公楼'), ('chejian', '车间'), ('shigongxianchang', '施工现场'), ('aita', '其他')], string='工作场所')
    beizhu = fields.Text('备注')
    yuangong = fields.One2many('hr.employee', 'job_id')
    state = fields.Selection([('draft', '起草'), ('confirmed', '岗位确认建立')], string='状态', default='draft')




