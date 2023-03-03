from odoo import models, fields, api

class Universite(models.Model):

    _name = "amicales.universite"

    nomUniversite = fields.Char(
        string='nomUniversite',
    )
    
    adresse = fields.Char(
        string='adresse',
    )
    
    faculte_ids = fields.One2many('amicales.faculte.xml','universite_id',string='facultes',)
    
    
    