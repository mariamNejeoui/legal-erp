from odoo import models, fields

class LegalActivity(models.Model):
    _name = 'legal.activity'
    _description = 'Legal Activity'

    # --- Basic Fields ---
    description = fields.Text(string='Description', required=True)
    
    # default=fields.Date.context_today hace que por defecto ponga la fecha actual
    date = fields.Date(string='Date', required=True, default=fields.Date.context_today)
    
    # Double in ER diagram becomes Float in Odoo
    hours_spent = fields.Float(string='Hours Spent', required=True)
    
    # Selection field for the integer activity_type
    activity_type = fields.Selection([
        ('consultation', 'Consultation'),
        ('drafting', 'Document Drafting'),
        ('court', 'Court Appearance'),
        ('research', 'Research'),
        ('meeting', 'Meeting')
    ], string='Activity Type', required=True)
    
    is_billable = fields.Boolean(string='Is Billable', default=True)

    # --- FOREIGN KEYS (Relations) ---
    
    # FK: case_id -> Conecta con el expediente
    case_id = fields.Many2one(
        'legal.case', 
        string='Legal Case', 
        required=True, 
        ondelete='cascade'
    )
    
    # FK: lawyer_id -> Conecta con el usuario/abogado
    # El default hace que se auto-asigne al usuario que está logueado creando la actividad
    lawyer_id = fields.Many2one(
        'res.users', 
        string='Lawyer', 
        required=True,
        default=lambda self: self.env.user,
        ondelete='restrict'
    )
    
    # FK: invoice_id -> ¡Conectado al módulo de facturación nativo de Odoo!
    invoice_id = fields.Many2one(
        'account.move', 
        string='Invoice', 
        readonly=True, # Solo lectura, se rellenará automáticamente cuando se facture
        ondelete='set null'
    )