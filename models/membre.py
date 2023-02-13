from odoo import models, fields, api

class Membre(models.Model):

    _inherit = "amicales.etudiant"
    _name = "amicales.membre"

    
    matricule = fields.Char(
        string='matricule',
    )
    
    role = fields.Selection([('President', 'President'), ('Vice president', 'Vice president'),('Secretaire','Secretiare'),
                             ('Secretiare Adjoint','Secretiare Adjoint'),('Tresorier','Tresorier'),
                             ('Tresorier Adjoint','Tresorier Adjoint')],default='simple etudiant')
    
    commission_id = fields.Many2one('amicales.commission',string="commission")

    
    amicale_id = fields.Many2one("amicales.amicale","amicale")
    
    
    