from odoo import models, fields, api
from werkzeug.security import check_password_hash,generate_password_hash
class Membre(models.Model):

    _inherit = "amicales.etudiant"
    _name = "amicales.membre"

    
    matricule = fields.Char(
        string='matricule',
    )
    
    role = fields.Selection([('President', 'President'), ('Vice president', 'Vice president'),('Secretaire','Secretiare'),
                             ('Secretiare Adjoint','Secretiare Adjoint'),('Tresorier','Tresorier'),
                             ('Tresorier Adjoint','Tresorier Adjoint'),('Simple etudiant','Simple etudiant')])
    
    commission_id = fields.Many2one('amicales.commission',string="commission")

    role_id = fields.Many2one('amicales.role', string='role')

    
    amicale_id = fields.Many2one("amicales.amicale",string="amicale")

    @api.model
    def create(self, vals):
        """
        Hacher le mot de passe avant de créer un nouvel utilisateur.
        """
        if vals.get('password'):
            vals['password'] = generate_password_hash(vals['password'])

        """
        Affectation d'un role à l'utilisateur
        """
        if vals.get('fonction') == "President" or vals.get("Vice president"):
            role = vals.get('role_id', False)
            if not role:
                vals['role_id'] = 1
        elif vals.get('fonction') == "Secretaire" or vals.get("Secretaire Adjoint"):
            role = vals.get('role_id', False)
            if not role:
                vals['role_id'] = 2
        elif vals.get('fonction') == "Tresorier" or vals.get("Tresorier Adjoint"):
            role = vals.get('role_id', False)
            if not role:
                vals['role_id'] = 3
        else:
            role = vals.get('role_id', False)
            if not role:
                vals['role_id'] = 4
        return super(Membre, self).create(vals)

    def check_password(self, password):
        return check_password_hash(self.password, password)



    def action_confirme_mail(self):
        template = self.env.ref('amicales.email_template_membre')
        template.sudo().send_mail(self.id, force_send=True, raise_exception=True)
    
    