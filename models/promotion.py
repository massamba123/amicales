from odoo import models, fields, api

class Promotion(models.Model):

    _name = "amicales.promotion"

    promotion = fields.Char(string="promotion")
    datePromo = fields.Date(string='data_promo')
    description = fields.Char(string="description")
    niveau_id = fields.Many2one("amicales.niveau",string="niveau")
    etudiant_ids = fields.One2many("amicales.etudiant","promotion_id",string="etudiants")