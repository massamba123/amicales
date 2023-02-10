from odoo import models, fields, api

class Etudiant(models.Model):

    _name = "amicales.etudiant"

    prenom = fields.Char(string="prenom")
    nom = fields.Char(string="nom")
    age = fields.Char(string="age")
    telephone = fields.Char(string="telephone")
    adresse = fields.Char(string="adresse")
    niveau_id = fields.Many2one("amicales.niveau",string="niveau")
    departement_id = fields.Many2one("amicales.departement",string="departement")
    promotion_id = fields.Many2one("amicales.promotion",string="promotion")