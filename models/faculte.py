from odoo import models, fields, api

class Faculte(models.Model):

    _name = "amicales.faculte"

    
    nomFaculte = fields.Char(
        string='nomFaculte',
    )
    universite_id = fields.Many2one('amicales.universite',string='universite')
    
    departement_ids = fields.One2many("amicales.departement","faculte_id",string='departements')