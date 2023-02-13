from odoo import models, fields, api

class Commission(models.Model):

    _name = "amicales.commission"

    
    nomCommission = fields.Char(
        string='nomCommission',
    )
    
    membre_ids = fields.One2many('amicales.membre','commission_id',string='membres')

    amicale_id = fields.Many2one("amicales.amicale","amicale")
