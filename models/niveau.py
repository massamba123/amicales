from odoo import models, fields, api

class Niveau(models.Model):

    _name = "amicales.niveau"

    
    niveau = fields.Char(
        string='niveau',
    )
    
    departement_id = fields.Many2one("amicales.departement",string='departement')
    promotion_ids = fields.One2many("amicales.promotion","niveau_id",string="promotions")
    

    