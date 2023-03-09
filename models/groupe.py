from odoo import models, fields, api

class Groupe(models.Model):
    _name = "amicales.groupe"

    nomGroupe = fields.Char(string="nomGroupe")
    role_id = fields.Many2one('amicales.role',string='role')