# -*- coding: utf-8 -*-
{
    'name': 'Sherart_customizations',
    'version': '13.0.1.0.0',
    'description': """
    Customizations made for Sherart.
    """,
    'author': "Alpiek",
    'website': "https://alpiek.nl/",
    'depends': [
        'mrp',
    ],
    'data': [
        'views/mrp_overview.xml',
    ],
    'qweb': [
        'contacts',
        'delivery',
        'product',
        'static/src/xml/mrp_mps.xml',
        'static/src/xml/sync_data_button.xml',
    ],
    'application': False,
    'license': u'OPL-1',
}
