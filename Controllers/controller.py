from odoo import http
from odoo.http import request
from odoo.exceptions import AccessDenied
from werkzeug.utils import redirect

class Controller(http.Controller):

    @http.route('/web/login', type='http', auth='public', csrf=False)
    def custom_logins(self, **kw):
        telephone = kw.get('login')
        password = kw.get('password')
        if telephone and password:
            user = request.env['amicales.membre'].sudo().search([('telephone', '=', telephone)])
            role1 = request.env['amicales.role'].sudo().search([('id', '=', 1)])
            role2 = request.env['amicales.role'].sudo().search([('id', '=', 2)])
            if user and user.check_password(password):
                # request.session['admin'] = user.telephone
                if user.role_id == role1:
                    return request.redirect('/admin')
                elif user.role_id == role2:
                    return request.redirect("/amicales")
            raise AccessDenied()
    @http.route('/amicales',type='http', auth='public', website=True)
    def index(self, **kwargs):
        return request.render("amicales.index")

    @http.route('/organigramme', type='http', auth='public', website=True)
    def organigramme(self, **kwargs):
        return request.render("amicales.organigramme")

    @http.route('/login', type='http', auth='public', website=True)
    def amicale(self, **kwargs):
        return request.render("amicales.logindex")

    @http.route('/a_propos', type='http', auth='public', website=True)
    def a_propos(self, **kwargs):
        return request.render("amicales.a_propos")
    @http.route('/fairedon', type='http', auth='public', website=True)
    def fairedon(self, **kwargs):
        return request.render("amicales.fairedon")

    @http.route('/programme', type='http', auth='public', website=True)
    def programme(self, **kwargs):
        return request.render("amicales.programme")

    @http.route('/admin', type='http', auth='public', website=True, csrf=False)
    def Fadmin_list_page(self, **kwargs):
        etudiant_obj = request.env['amicales.etudiant']
        etudiants = etudiant_obj.search([])
        membre_obj = request.env['amicales.membre']
        membres = membre_obj.search([])
        universite_obj = request.env['amicales.universite']
        universites = universite_obj.search([])
        faculte_obj = request.env['amicales.faculte']
        facultes = faculte_obj.search([])
        departement_obj = request.env['amicales.departement']
        departements = departement_obj.search([])
        promotion_obj = request.env['amicales.promotion']
        promotions = promotion_obj.search([])
        niveau_obj = request.env['amicales.niveau']
        niveaux = niveau_obj.search([])
        commission_obj = request.env['amicales.commission']
        commissions = commission_obj.search([])
        amicale_obj = request.env['amicales.amicale']
        amicales = amicale_obj.search([])
        amicale_obj = request.env['amicales.role']
        roles = amicale_obj.search([])


        return http.request.render('amicales.gestion_amicale', {
            'etudiants': etudiants,
            'membres': membres,
            'universites': universites,
            'facultes': facultes,
            'departements': departements,
            'promotions': promotions,
            'niveaux': niveaux,
            'commissions': commissions,
            'amicales': amicales,
            'roles':roles,


        })

    @http.route('/createU', type='http', auth="public", website=True, csrf=False)
    def create_universite(self, **post):
        Universite = request.env['amicales.universite']
        universite = Universite.create(post)
        return request.redirect('/admin')

    @http.route('/formU', type='http', auth="public", website=True)
    def universite_form(self, **kw):

        return request.render('amicales.createuniversite', {
        })

    @http.route('/createF', type='http', auth="public", website=True, csrf=False)
    def create_faculte(self, **post):
        Faculte = request.env['amicales.faculte']
        faculte = Faculte.create(post)
        return request.redirect('/admin')

    @http.route('/formF', type='http', auth="public", website=True)
    def faculte_form(self, **kw):
        Universite = request.env['amicales.universite']
        return request.render('amicales.createfaculte', {

            'universites': Universite.search([]),
        })

    @http.route('/createE', type='http', auth="public", website=True, csrf=False)
    def create_etudiant(self, **post):
        Etudiant = request.env['amicales.etudiant']
        etudiant = Etudiant.create(post)
        etudiant.confirme_mail()
        return request.redirect('/amicales')

    @http.route('/formE', type='http', auth="public", website=True)
    def etudiant_form(self, **kw):
        Departement = request.env['amicales.departement']
        Niveau = request.env['amicales.niveau']
        Promotion = request.env['amicales.promotion']
        Role = request.env['amicales.role']
        return request.render('amicales.createetudiant', {
            'departements': Departement.search([]),
            'niveaux': Niveau.search([]),
            'promotions': Promotion.search([]),
            'roles': Role.search([]),
        })

    @http.route('/createAd', type='http', auth="public", website=True, csrf=False)
    def ad_etudiant(self, **post):
        Etudiant = request.env['amicales.etudiant']
        etudiant = Etudiant.create(post)
        etudiant.confirme_mail()
        return request.redirect('/amicales')

    @http.route('/formAd', type='http', auth="public", website=True)
    def ad_form(self, **kw):
        Departement = request.env['amicales.departement']
        Niveau = request.env['amicales.niveau']
        Promotion = request.env['amicales.promotion']
        return request.render('amicales.createetudiantadherer', {
            'departements': Departement.search([]),
            'niveaux': Niveau.search([]),
            'promotions': Promotion.search([]),
        })

    @http.route('/createM', type='http', auth="public", website=True, csrf=False)
    def create_membre(self, **post):
        Membre = request.env['amicales.membre']
        membre = Membre.create(post)
        membre.action_confirme_mail()
        return request.redirect('/admin')

    @http.route('/formM', type='http', auth="public", website=True)
    def membre_form(self, **kw):
        Departement = request.env['amicales.departement']
        Niveau = request.env['amicales.niveau']
        Promotion = request.env['amicales.promotion']
        Commission = request.env['amicales.commission']
        Amicale = request.env['amicales.amicale']
        Role = request.env['amicales.role']
        return request.render('amicales.createmembre', {
            'departements': Departement.search([]),
            'niveaux': Niveau.search([]),
            'promotions': Promotion.search([]),
            'commissions': Commission.search([]),
            'amicales': Amicale.search([]),
            'roles': Role.search([]),
        })




    @http.route('/createD', type='http', auth="public", website=True, csrf=False)
    def create_departement(self, **post):
        Departement = request.env['amicales.departement']
        departement = Departement.create(post)
        return request.redirect('/admin')

    @http.route('/formD', type='http', auth="public", website=True)
    def departement_form(self, **kw):
        Faculte = request.env['amicales.faculte']
        Niveau = request.env['amicales.niveau']
        return request.render('amicales.createdepartement', {

            'facultes': Faculte.search([]),
            'niveaux': Niveau.search([]),
        })

    @http.route('/createN', type='http', auth="public", website=True, csrf=False)
    def create_niveau(self, **post):
        Niveau = request.env['amicales.niveau']
        niveau = Niveau.create(post)
        return request.redirect('/admin')

    @http.route('/formN', type='http', auth="public", website=True)
    def niveau_form(self, **kw):
        Departement = request.env['amicales.departement']

        return request.render('amicales.createniveau', {

            'departements': Departement.search([]),

        })

    @http.route('/createP', type='http', auth="public", website=True, csrf=False)
    def create_promotion(self, **post):
        Promotion = request.env['amicales.promotion']
        promotion = Promotion.create(post)
        return request.redirect('/admin')

    @http.route('/formP', type='http', auth="public", website=True)
    def promotion_form(self, **kw):
        Niveau = request.env['amicales.niveau']

        return request.render('amicales.createpromotion', {

            'niveaux': Niveau.search([]),

        })

    @http.route('/createC', type='http', auth="public", website=True, csrf=False)
    def create_commission(self, **post):
        Commission = request.env['amicales.commission']
        commission = Commission.create(post)
        return request.redirect('/admin')

    @http.route('/formC', type='http', auth="public", website=True)
    def commission_form(self, **kw):
        Amicale = request.env['amicales.amicale']

        return request.render('amicales.createcommission', {

            'amicales': Amicale.search([]),

        })

    @http.route('/createA', type='http', auth="public", website=True, csrf=False)
    def create_commission(self, **post):
        Amicale = request.env['amicales.amicale']
        amicale = Amicale.create(post)
        return request.redirect('/admin')

    @http.route('/formA', type='http', auth="public", website=True)
    def commission_form(self, **kw):


        return request.render('amicales.createamicale', {



        })

    @http.route('/admin/<int:etudiant_id>', type='http', auth='public', website=True)
    def etudiant_supprimer(self, etudiant_id, **post):
        Etudiant = request.env['amicales.etudiant']
        etudiant = Etudiant.browse(etudiant_id)
        etudiant.unlink()
        return request.redirect('/admin')

    @http.route('/modifierE', type='http', auth='public', website=True, csrf=False)
    def etudiant_modifier(self, etudiant_id=None, prenom=None, nom=None, age=None,mail=None, telephone=None, adresse=None,
                          departement_id=None, niveau_id=None, **post):
        Etudiant = request.env['amicales.etudiant']
        etudiant = Etudiant.browse(int(etudiant_id))
        etudiant.write({
            'prenom': prenom,
            'nom': nom,
            'age': int(age),
            'mail':mail,
            'telephone': telephone,
            'adresse': adresse,
            'departement_id': int(departement_id),
            'niveau_id': int(niveau_id)
        })
        return request.redirect('/admin')

    @http.route('/etudiant<int:etudiant_id>', type='http', auth='public', website=True)
    def etudiant_afficher_modifier(self, etudiant_id, **post):
        Etudiant = request.env['amicales.etudiant']
        etudiant = Etudiant.browse(etudiant_id)
        Departement = request.env['amicales.departement']
        departements = Departement.search([])
        Niveau = request.env['amicales.niveau']
        niveaux = Niveau.search([])
        return request.render('amicales.modifieretudiant',
                              {'etudiant': etudiant, 'departements': departements, 'niveaux': niveaux})

    @http.route('/admin/<int:universite_id>', type='http', auth='public', website=True)
    def universite_supprimer(self, universite_id, **post):
        Universite = request.env['amicales.universite']
        universite = Universite.browse(universite_id)
        universite.unlink()
        return request.redirect('/admin')
    @http.route('/modifierU', type='http', auth='public', website=True, csrf=False)
    def universite_modifier(self, universite_id=None, nomUniversite=None, adresse=None, **post):
        Universite = request.env['amicales.universite']
        universite = Universite.browse(int(universite_id))
        universite.write({
            'nomUniversite': nomUniversite,
            'adresse': adresse,
        })
        return request.redirect('/admin')

    @http.route('/universite<int:universite_id>', type='http', auth='public', website=True)
    def universite_afficher_modifier(self, universite_id, **post):
        Universite = request.env['amicales.universite']
        universite = Universite.browse(universite_id)
        return request.render('amicales.modifieruniversite', {
            'universite': universite
        })

    @http.route('/faculte/supprimer/<int:faculte_id>', type='http', auth='public', website=True)
    def faculte_supprimer(self, faculte_id, **post):
        Faculte = request.env['amicales.faculte']
        faculte = Faculte.browse(faculte_id)
        faculte.unlink()
        return request.redirect('/admin')

    @http.route('/modifierF', type='http', auth='public', website=True, csrf=False)
    def faculte_modifier(self, faculte_id=None,nomFaculte=None, universite_id=None,  **post):
        Faculte = request.env['amicales.faculte']
        faculte = Faculte.browse(int(faculte_id))
        faculte.write({
            'nomFaculte': nomFaculte,
            'universite_id':  int(universite_id),

        })
        return request.redirect('/admin')

    @http.route('/faculte<int:faculte_id>', type='http', auth='public', website=True)
    def faculte_afficher_modifier(self, faculte_id, **post):
        Faculte = request.env['amicales.faculte']
        faculte = Faculte.browse(faculte_id)
        Universite = request.env['amicales.universite']
        universites = Universite.search([])
        return request.render('amicales.modifierfaculte', {
            'faculte': faculte,
            'universites': universites,

        })
    @http.route('/departement/supprimer/<int:departement_id>', type='http', auth='public', website=True)
    def departement_supprimer(self, departement_id, **post):
        Departement = request.env['amicales.departement']
        departement = Departement.browse(departement_id)
        departement.unlink()
        return request.redirect('/admin')

    @http.route('/modifierD', type='http', auth='public', website=True, csrf=False)
    def departement_modifier(self, departement_id=None,nomDepartement=None, faculte_id=None,  **post):
        Departement = request.env['amicales.departement']
        departement = Departement.browse(int(departement_id))
        departement.write({
            'nomDepartement': nomDepartement,
            'faculte_id': int(faculte_id),


        })
        return request.redirect('/admin')

    @http.route('/departement<int:departement_id>', type='http', auth='public', website=True)
    def departement_afficher_modifier(self, departement_id, **post):
        Departement = request.env['amicales.departement']
        departement = Departement.browse(departement_id)
        Faculte = request.env['amicales.faculte']
        facultes = Faculte.search([])
        return request.render('amicales.modifierdepartement', {
            'departement': departement,
            'facultes': facultes,

        })

    @http.route('/niveau/supprimer/<int:niveau_id>', type='http', auth='public', website=True)
    def niveau_supprimer(self, niveau_id, **post):
        Niveau = request.env['amicales.niveau']
        niveau = Niveau.browse(niveau_id)
        niveau.unlink()
        return request.redirect('/admin')

    @http.route('/modifierN', type='http', auth='public', website=True, csrf=False)
    def niveau_modifier(self, niveau_id=None, niveau=None, departement_id=None,  **post):
        Niveau = request.env['amicales.niveau']
        niveaut = Niveau.browse(int(niveau_id))
        niveaut.write({
            'niveau': niveau,
            'departement_id': int(departement_id),

        })
        return request.redirect('/admin')

    @http.route('/niveau<int:niveau_id>', type='http', auth='public', website=True)
    def niveau_afficher_modifier(self, niveau_id, **post):
        Niveau = request.env['amicales.niveau']
        niveau = Niveau.browse(niveau_id)
        Departement = request.env['amicales.departement']
        departements = Departement.search([])
        return request.render('amicales.modifierniveau', {
            'niveau': niveau,
            'departements': departements,

        })

    @http.route('/promotion/supprimer/<int:promotion_id>', type='http', auth='public', website=True)
    def promotion_supprimer(self, promotion_id, **post):
        Promotion = request.env['amicales.promotion']
        promotion = Promotion.browse(promotion_id)
        promotion.unlink()
        return request.redirect('/admin')

    @http.route('/modifierP', type='http', auth='public', website=True, csrf=False)
    def promotion_modifier(self, promotion_id=None, promotion=None,datePromo=None,description=None, niveau_id=None, **post):
        Promotion = request.env['amicales.promotion']
        promotiont = Promotion.browse(int(promotion_id))
        promotiont.write({
            'promotion': promotion,
            'datePromo':datePromo,
            'description':description,
            'niveau_id': int(niveau_id),

        })
        return request.redirect('/admin')

    @http.route('/promotion<int:promotion_id>', type='http', auth='public', website=True)
    def promotion_afficher_modifier(self, promotion_id, **post):
        Promotion = request.env['amicales.promotion']
        promotion = Promotion.browse(promotion_id)
        Niveau = request.env['amicales.niveau']
        niveaux = Niveau.search([])
        return request.render('amicales.modifierpromotion', {
            'promotion':promotion,
            'niveaux': niveaux,

        })

    @http.route('/amicale/supprimer/<int:amicale_id>', type='http', auth='public', website=True)
    def amicale_supprimer(self, amicale_id, **post):
        Amicale = request.env['amicales.amicale']
        amicale = Amicale.browse(amicale_id)
        amicale.unlink()
        return request.redirect('/amicale_tree')

    @http.route('/modifierA', type='http', auth='public', website=True, csrf=False)
    def amicale_modifier(self, amicale_id=None, nomAmicale=None, **post):
        Amicale = request.env['amicales.amicale']
        amicale = Amicale.browse(int(amicale_id))
        amicale.write({
            'nomAmicale': nomAmicale,


        })
        return request.redirect('/admin')

    @http.route('/amicale<int:amicale_id>', type='http', auth='public', website=True)
    def amicale_afficher_modifier(self, amicale_id, **post):
        Amicale= request.env['amicales.amicale']
        amicale = Amicale.browse(amicale_id)

        return request.render('amicales.modifieramicale', {
            'amicale': amicale,

        })

    @http.route('/commission/supprimer/<int:commission_id>', type='http', auth='public', website=True)
    def commission_supprimer(self, commission_id, **post):
        Commission = request.env['amicales.commission']
        commission = Commission.browse(commission_id)
        commission.unlink()
        return request.redirect('/admin')

    @http.route('/modifierC', type='http', auth='public', website=True, csrf=False)
    def commission_modifier(self, commission_id=None, nomCommission=None,amicale_id=None, **post):
        Commission= request.env['amicales.commission']
        commission = Commission.browse(int(commission_id))
        commission.write({
            'nomCommission': nomCommission,
            'amicale_id':amicale_id

        })
        return request.redirect('/admin')

    @http.route('/commission<int:commission_id>', type='http', auth='public', website=True)
    def commission_afficher_modifier(self, commission_id, **post):
        Commission = request.env['amicales.commission']
        commission = Commission.browse(commission_id)
        Amicale = request.env['amicales.amicale']
        amicales = Amicale.search([])
        return request.render('amicales.modifiercommission', {
            'commission': commission,
            'amicales':amicales,

        })

    @http.route('/membre/supprimer/<int:membre_id>', type='http', auth='public', website=True)
    def membre_supprimer(self, membre_id, **post):
        Membre = request.env['amicales.membre']
        membre = Membre.browse(membre_id)
        membre.unlink()
        return request.redirect('/admin')

    @http.route('/modifierM', type='http', auth='public', website=True, csrf=False)
    def membre_modifier(self, membre_id=None, prenom=None, nom=None, age=None, telephone=None, adresse=None,
                          departement_id=None, niveau_id=None, mail=None, matricule=None, role=None, commission_id=None, role_id=None,amicale_id=None, **post):
        Membre = request.env['amicales.membre']
        membre = Membre.browse(int(membre_id))
        membre.write({
            'prenom': prenom,
            'nom': nom,
            'age': int(age),
            'telephone': telephone,
            'adresse': adresse,
            'mail':mail,
            'departement_id': int(departement_id),
            'niveau_id': int(niveau_id),
            'role': role,
            'role_id': int(role_id),
            'matricule': matricule,
            'commission_id': commission_id,
            'amicale_id': amicale_id,

        })
        return request.redirect('/admin')

    @http.route('/membre<int:membre_id>', type='http', auth='public', website=True)
    def membre_afficher_modifier(self, membre_id, **post):
        Membre = request.env['amicales.membre']
        membre = Membre.browse(membre_id)
        Departement = request.env['amicales.departement']
        departements = Departement.search([])
        Niveau = request.env['amicales.niveau']
        niveaux = Niveau.search([])
        Commission = request.env['amicales.commission']
        commissions = Commission.search([])
        Amicale = request.env['amicales.amicale']
        amicales = Amicale.search([])
        Role = request.env['amicales.role']
        roles = Role.search([])

        return request.render('amicales.modifiermembre',
                              {'membre': membre,
                               'departements': departements,
                               'niveaux': niveaux,
                               'commissions': commissions,
                               'amicales': amicales,
                               'roles': roles,
                               })


