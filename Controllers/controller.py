from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

class Controller(http.Controller):

    @http.route('/',type='http', auth='public', website=True)
    def index(self, **kwargs):
        return request.render("amicales.index")

    # @http.route('/', type='http', auth='public', website=True)
    # def acceuil(self, **kwargs):
    #     return redirect('/')

    @http.route('/amicale', type='http', auth='public', website=True)
    def amicale(self, **kwargs):
        return request.render("amicales.amicale")

    @http.route('/a_propos', type='http', auth='public', website=True)
    def a_propos(self, **kwargs):
        return request.render("amicales.a_propos")
    @http.route('/fairedon', type='http', auth='public', website=True)
    def fairedon(self, **kwargs):
        return request.render("amicales.fairedon")

    @http.route('/membre', type='http', auth='public', website=True)
    def membre(self, **kwargs):
        return request.render("amicales.membre")

    @http.route('/programme', type='http', auth='public', website=True)
    def programme(self, **kwargs):
        return request.render("amicales.programme")

    @http.route('/etudiant', type='http', auth='public', website=True)
    def etudiant_page(self, **kwargs):
        etudiant_obj = request.env['amicales.etudiant']
        etudiants = etudiant_obj.search([])
        return http.request.render('amicales.etudiant_template', {'etudiants': etudiants})

    @http.route('/adherer', type='http', auth='public', website=True)
    def membre_page(self, **kwargs):
        membre_obj = request.env['amicales.membre']
        membres = membre_obj.search([])
        return http.request.render('amicales.membre_template', {'membres': membres})

    @http.route('/admin', type='http', auth='public', website=True)
    def admin_page(self, **kwargs):

        return http.request.render('amicales.template_admin', {})

    @http.route('/universite', type='http', auth='public', website=True)
    def universite_page(self, **kwargs):
        universite_obj = request.env['amicales.universite']
        universites = universite_obj.search([])
        return http.request.render('amicales.universite_template', {'universites': universites})

    @http.route('/faculte', type='http', auth='public', website=True)
    def faculte_page(self, **kwargs):
        faculte_obj = request.env['amicales.faculte']
        facultes = faculte_obj.search([])
        return http.request.render('amicales.faculte_template', {'facultes': facultes})

    @http.route('/departement', type='http', auth='public', website=True)
    def departement_page(self, **kwargs):
        departement_obj = request.env['amicales.departement']
        departements = departement_obj.search([])
        return http.request.render('amicales.departement_template', {'departements': departements})

    @http.route('/promotion', type='http', auth='public', website=True)
    def promotion_page(self, **kwargs):
        promotion_obj = request.env['amicales.promotion']
        promotions = promotion_obj.search([])
        return http.request.render('amicales.promotion_template', {'promotions': promotions})

    @http.route('/niveau', type='http', auth='public', website=True)
    def niveau_page(self, **kwargs):
        niveau_obj = request.env['amicales.niveau']
        niveaux = niveau_obj.search([])
        return http.request.render('amicales.niveau_template', {'niveaux': niveaux})

    @http.route('/commission', type='http', auth='public', website=True)
    def commission_page(self, **kwargs):
        commission_obj = request.env['amicales.commission']
        commissions = commission_obj.search([])
        return http.request.render('amicales.commission_template', {'commissions': commissions})

    @http.route('/amicale_tree', type='http', auth='public', website=True)
    def amicale_page(self, **kwargs):
        amicale_obj = request.env['amicales.amicale']
        amicales = amicale_obj.search([])
        return http.request.render('amicales.amicale_template', {'amicales': amicales})

    @http.route('/createE', type='http', auth="public", website=True, csrf=False)
    def create_etudiant(self, **post):
        Etudiant = request.env['amicales.etudiant']
        etudiant = Etudiant.create(post)
        return request.redirect('/etudiant')

    @http.route('/formE', type='http', auth="public", website=True)
    def etudiant_form(self, **kw):
        Departement = request.env['amicales.departement']
        Niveau = request.env['amicales.niveau']
        Promotion = request.env['amicales.promotion']
        return request.render('amicales.createetudiant', {
            'departements': Departement.search([]),
            'niveaux': Niveau.search([]),
            'promotions': Promotion.search([]),
        })

    @http.route('/createM', type='http', auth="public", website=True, csrf=False)
    def create_membre(self, **post):
        Membre = request.env['amicales.membre']
        membre = Membre.create(post)
        return request.redirect('/adherer')

    @http.route('/formM', type='http', auth="public", website=True)
    def membre_form(self, **kw):
        Departement = request.env['amicales.departement']
        Niveau = request.env['amicales.niveau']
        Promotion = request.env['amicales.promotion']
        Commission = request.env['amicales.commission']
        Amicale = request.env['amicales.amicale']
        return request.render('amicales.createmembre', {
            'departements': Departement.search([]),
            'niveaux': Niveau.search([]),
            'promotions': Promotion.search([]),
            'commissions': Commission.search([]),
            'amicales': Amicale.search([]),
        })

    @http.route('/createU', type='http', auth="public", website=True, csrf=False)
    def create_universite(self, **post):
        Universite = request.env['amicales.universite']
        universite = Universite.create(post)
        return request.redirect('/universite')

    @http.route('/formU', type='http', auth="public", website=True)
    def universite_form(self, **kw):
        Faculte = request.env['amicales.faculte']
        return request.render('amicales.createuniversite', {

            'facultes': Faculte.search([]),
        })

    @http.route('/createF', type='http', auth="public", website=True, csrf=False)
    def create_faculte(self, **post):
        Faculte = request.env['amicales.faculte']
        faculte = Faculte.create(post)
        return request.redirect('/faculte')

    @http.route('/formF', type='http', auth="public", website=True)
    def faculte_form(self, **kw):
        Universite = request.env['amicales.universite']
        Departement = request.env['amicales.departement']
        return request.render('amicales.createfaculte', {

            'departements': Departement.search([]),
            'universites': Universite.search([]),
        })

    @http.route('/createD', type='http', auth="public", website=True, csrf=False)
    def create_departement(self, **post):
        Departement = request.env['amicales.departement']
        departement = Departement.create(post)
        return request.redirect('/departement')

    @http.route('/formD', type='http', auth="public", website=True)
    def departement_form(self, **kw):
        Faculte = request.env['amicales.faculte']
        Niveau = request.env['amicales.niveau']
        return request.render('amicales.createdepartement', {

            'facultes': Faculte.search([]),
            'niveaux': Niveau.search([]),
        })

    @http.route('/createN', type='http', auth="public", website=True, csrf=False)
    def create_niveau(self, **post):
        Niveau = request.env['amicales.niveau']
        niveau = Niveau.create(post)
        return request.redirect('/niveau')

    @http.route('/formN', type='http', auth="public", website=True)
    def niveau_form(self, **kw):
        Departement = request.env['amicales.departement']

        return request.render('amicales.createniveau', {

            'departements': Departement.search([]),

        })

    @http.route('/createP', type='http', auth="public", website=True, csrf=False)
    def create_promotion(self, **post):
        Promotion = request.env['amicales.promotion']
        promotion = Promotion.create(post)
        return request.redirect('/promotion')

    @http.route('/formP', type='http', auth="public", website=True)
    def promotion_form(self, **kw):
        Niveau = request.env['amicales.niveau']

        return request.render('amicales.createpromotion', {

            'niveaux': Niveau.search([]),

        })

    @http.route('/createC', type='http', auth="public", website=True, csrf=False)
    def create_commission(self, **post):
        Commission = request.env['amicales.commission']
        commission = Commission.create(post)
        return request.redirect('/commission')

    @http.route('/formC', type='http', auth="public", website=True)
    def commission_form(self, **kw):
        Amicale = request.env['amicales.amicale']

        return request.render('amicales.createcommission', {

            'amicales': Amicale.search([]),

        })

    @http.route('/createA', type='http', auth="public", website=True, csrf=False)
    def create_commission(self, **post):
        Amicale = request.env['amicales.amicale']
        amicale = Amicale.create(post)
        return request.redirect('/amicale_tree')

    @http.route('/formA', type='http', auth="public", website=True)
    def commission_form(self, **kw):


        return request.render('amicales.createamicale', {



        })
