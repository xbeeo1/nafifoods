# -*- coding: utf-8 -*-
{
    "name": "Xbo Nafi Custom",

    'version': '19.0.0.0',

    'summary': """Xbo Nafi Custom""",

    'description': """Xbo Nafi Custom""",

    'category': 'custom',

    'author': "Xbeeo",

    'website': 'https://xbeeo.com/',

    "depends": ['base','sale','account'],

    "data": [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/booker_margin_views.xml',
        'views/distributor_margin_views.xml',
        'views/trade_offer_views.xml',

    ],

}
