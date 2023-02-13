from odoo import models, fields, api

class Amicale(models.Model):

    _name = "amicales.amicale"

    
    nomAmicale = fields.Char(
        string='nomAmicale',
    )
    
    membre_ids = fields.One2many("amicales.membre","amicale_id","membres")

    
    commision_ids = fields.One2many("amicales.commission","amicale_id","commissions")
    
    
    