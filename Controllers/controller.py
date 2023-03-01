from odoo import http
from odoo.http import request

class Controller(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def index(self, **kwargs):
        return request.render("amicales.index")