from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

class Controller(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
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
        return http.request.render('amicales.membre_template', {'membre': membres})

    @http.route('/universite', type='http', auth='public', website=True)
    def universite_page(self, **kwargs):
        universite_obj = request.env['amicales.universite']
        universites = universite_obj.search([])
        return http.request.render('amicales.universite_template', {'universite': universites})

    @http.route('/faculte', type='http', auth='public', website=True)
    def faculte_page(self, **kwargs):
        faculte_obj = request.env['amicales.faculte']
        facultes = faculte_obj.search([])
        return http.request.render('amicales.faculte_template', {'faculte': facultes})

    @http.route('/amicales/etudiant/create', type='http', auth="public", website=True)
    def create_etudiant(self, **post):
        Etudiant = request.env['amicales.etudiant']
        etudiant = Etudiant.create(post)
        return request.redirect('/amicales/etudiant/%d' % etudiant.id)

    @http.route('/amicales/etudiant/form', type='http', auth="public", website=True, csrf=False)
    def etudiant_form(self, **kw):
        Departement = request.env['amicales.departement']
        Niveau = request.env['amicales.niveau']
        Promotion = request.env['amicales.promotion']
        return request.render('amicales.amicales_etudiant_create_form', {
            'departements': Departement.search([]),
            'niveaux': Niveau.search([]),
            'promotions': Promotion.search([]),
        })

