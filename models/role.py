from odoo import models, fields, api

class Role(models.Model):
    _name = "amicales.role"

    nomRole = fields.Char(string="nomRole")
    groupe_ids = fields.One2many('amicales.groupe','role_id',string='groupes')
    membre_ids = fields.One2many('amicales.membre','role_id',string='membres')