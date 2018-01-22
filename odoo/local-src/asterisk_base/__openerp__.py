{
    'name': 'Odoo Asterisk Management Base Application',
    'summary': '',
    'description': """Use Odoo to Manage your Asterisk.""",
    'version': '1.0',
    'category': 'Telephony',
    'author': 'Communicom',
    'website': 'http://communicom.ru',
    'depends': ['web', 'bus'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/conf.xml',
        'views/server.xml',
        'views/channel.xml',
        'views/settings.xml',
        # Data files
        'data/server.xml', # Must be the first data view to import.
        'data/ari_conf.xml',
        'data/features_conf.xml',
        'data/http_conf.xml',
        'data/manager_conf.xml',
        'data/modules_conf.xml',
        'data/extensions_conf.xml',
        'data/sip_conf.xml',
        'data/cdr_conf.xml',
        'data/cel_conf.xml',
        'data/cel_odbc_conf.xml',
    ],
    'demo': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
}
