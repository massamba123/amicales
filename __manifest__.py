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
        'templates/Membre/membre_create.xml',
        'templates/Membre/membre.xml',
        'templates/Membre/membre_modif.xml',
         'templates/etudiant/etudiant.xml',
         'templates/etudiant/etudiant_create.xml',
        'templates/etudiant/adherer.xml',

         'templates/etudiant/etudiant_modif.xml',
        'templates/Universite/universite.xml',
        'templates/Universite/universite_create.xml',
        'templates/Universite/universite_modif.xml',
        'templates/Faculte/faculte.xml',
        'templates/Faculte/faculte_create.xml',
        'templates/Faculte/faculte_modifi.xml',
        'templates/Promotion/promotion.xml',
        'templates/Promotion/promotion_create.xml',
        'templates/Promotion/promotion_modif.xml',
        'templates/Niveau/niveau.xml',
        'templates/Niveau/niveau_create.xml',
        'templates/Niveau/niveau_modif.xml',
        'templates/Departement/departement.xml',
        'templates/Departement/departement_modif.xml',
        'templates/Departement/departement_create.xml',
        'templates/Commission/commission.xml',
        'templates/Commission/commission_create.xml',
        'templates/Commission/commission_modif.xml',
        'templates/Amicale/amicale.xml',
        'templates/Amicale/amicale_create.xml',
        'templates/Amicale/amicale_modif.xml',
        'templates/index.xml',
        'templates/login.xml',
        'templates/a_propos.xml',
        'templates/organigramme.xml',
        'templates/fairedon.xml',
        'templates/gestion_amicale.xml',
        'templates/programme.xml',
        'templates/amicales/header.xml',
        'templates/amicales/footer.xml',


    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': ['static/src/xml/*.xml', 'static/src/xml/assets_backend.xml',],
    'license': 'LGPL-3',
    'images':['/static/src/images/'],
     'assets': {
            'web.assets_frontend': [
                'amicales/static/js/script.js',
            ],
     }



}
