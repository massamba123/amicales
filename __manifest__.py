# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Amicales',
    'version': '16.0',
    'category': 'TDSI',
    'summary': 'AmicaleKS',
    'description': "",
    'website': 'https://www.odoo.com/page/mescourse',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/universite_views.xml',
        'views/faculte_views.xml',
        'views/departement_views.xml',
        'views/niveau_views.xml',
        'views/promotion_views.xml',
        'views/etudiant_views.xml',
        'views/membre_views.xml',
        'views/commission_views.xml',
        'views/amicale_views.xml',
        'templates/index.xml',
        'templates/amicale.xml',
        'templates/a_propos.xml',
        'templates/fairedon.xml',
        'templates/membre.xml',
        'templates/programme.xml',
        'templates/header.xml',
        'templates/footer.xml',




    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
    'images':['/static/src/images/'],
}
