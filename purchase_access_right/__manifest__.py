# -*- coding: utf-8 -*-
{
    'name': "Purchase Access Right",

    'summary': """
        workflow for purchase
        """,

    'description': """
    """,

    'author': "Abuemira",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'purchase',
    'version': '15.1',

    # any module necessary for this one to work correctly
    'depends': ["base", "purchase", ],
    # always loaded
    'data': [
       #'security/ir.model.access.csv',
        'security/security.xml',
        'views/purchase_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
