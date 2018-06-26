{
    'name': 'Contact Positions',
    'version': '11.0.1.0',
    'licence': 'OPL-1',
    'category': 'Partner',
    'summary' : 'Create a custom job function for the res.partner contacts',
    'description': """
    """,
    'author': 'Confianz IT',
    'website': 'http://www.confianzit.biz',
    'maintainer': 'Confianz IT',
    'depends': ['sale', 'crm', 'hr', 'partner_firstname', 'contacts', ],
    'data': [
        'security/user_groups.xml',
        'views/view.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application' : True,
}
