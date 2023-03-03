from odoo import models, fields, api

class Departement(models.Model):
    _name = "amicales.departement"

    
    nomDepartement = fields.Char(
        string='nomDepartement',
    )
    
    faculte_id = fields.Many2one("amicales.faculte.xml",string='faculte.xml')
    niveau_ids = fields.One2many("amicales.niveau","departement_id",string='niveau')
    
    