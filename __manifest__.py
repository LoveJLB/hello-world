# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Directory',
    'version': '1.1',
    'category': 'Human Resources',
    'sequence': 75,
    'summary': 'Jobs, Departments, Employees Details',
    'description': """
Human Resources Management
==========================

This application enables you to manage important aspects of your company's staff and other details such as their skills, contacts, working time...


You can manage:
---------------
* Employees and hierarchies : You can define your employee with User and display hierarchies
* HR Departments
* HR Jobs
    """,
    'website': 'https://www.odoo.com/page/employees',
    'images': [
        'images/hr_department.jpeg',
        'images/hr_employee.jpeg',
        'images/hr_job_position.jpeg',
        'static/src/img/default_image.png',
    ],
    'depends': [
        'base_setup',
        'mail',
        'resource',
        'web_kanban',
    ],
    'data': [
        'security/hr_securityt.xml',
        'security/ir.model.access.csv',
        'views/hr_views.xml',
        'views/hr_templates.xml',
        'data/hr_data.xml',
        'views/employee_workflow.xml',
        'views/hetong_workflow.xml',
        'views/zhengzhao_workflow.xml',
        'views/shiyongkaohe_workflow.xml',
        'views/zhuanzengshenqing_workflow.xml',
        'views/tiaogangshenqing_workflow.xml',
        'views/renlixuqiu_workflow.xml',
        'views/lizhishenqing_workflow.xml',
        'views/jinshengshenqing_workflow.xml',
        'views/partment_workflow.xml',
        # 'views/zhize.xml',


    ],
    'demo': [
        'data/hr_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
