from odoo import models, fields, api

class Etudiant(models.Model):

    _name = "amicales.etudiant"

    prenom = fields.Char(string="prenom")
    nom = fields.Char(string="nom")
    age = fields.Char(string="age")
    telephone = fields.Char(string="telephone")
    mail = fields.Char(string="Mail", required=True)
    password = fields.Char(string="Password")

    adresse = fields.Char(string="adresse")
    niveau_id = fields.Many2one("amicales.niveau",string="niveau")
    departement_id = fields.Many2one("amicales.departement",string="departement")
    promotion_id = fields.Many2one("amicales.promotion",string="promotion")

    def confirme_mail(self):
        template = self.env.ref('amicales.email_template_etudiant')
        template.sudo().send_mail(self.id, force_send=True, raise_exception=True)
