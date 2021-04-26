# -*- coding: utf-8 -*-
{
    'name':        "My Demo",

    'summary':
                   """
                   My Demo
                   """,

    'description': """
        Description ...
    """,

    'author':      "Me",
    'website':     "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':    'My Demo',
    'version':     '0.1',

    # any module necessary for this one to work correctly
    'depends':     ['base', 'mail', 'crm'],

    # always loaded
    'data':        [
        "security/ir.model.access.csv",
        "views/demo_view.xml",
    ],
    # only loaded in demonstration mode
    'demo':        [
        # "demo/demo.xml"
    ],
    'license': 'AGPL-3',
    'application':True,
}
