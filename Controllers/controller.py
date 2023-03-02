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

