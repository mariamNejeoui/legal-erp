from odoo import models, fields

class ResClient(models.Model):
    _inherit = 'res.partner'

    # --- Filtro principal del ERP ---
    is_legal_client = fields.Boolean(string='Is a Legal Client', default=False)

    # 1. CAMPOS GENERALES (Tabla Client)
    registration_date = fields.Date(
        string='Registration Date', 
        default=fields.Date.context_today
    )
    
    risk_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Risk Level', default='low')
    
    due_diligence_completed = fields.Boolean(string='Due Diligence Completed', default=False)

    # 2. CAMPOS PERSONA FÍSICA (Tabla IndividualClient)
    national_id = fields.Char(string='National ID (DNI/Passport)')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Marital Status')
    
    birth_date = fields.Date(string='Birth Date')
    
    # Conectado a la tabla de países de Odoo
    nationality_id = fields.Many2one('res.country', string='Nationality')
    
    profession = fields.Char(string='Profession')

    # 3. CAMPOS EMPRESA (Tabla CorporateClient)
    industry_sector = fields.Char(string='Industry Sector')
    representative_name = fields.Char(string='Representative Name')
    representative_role = fields.Char(string='Representative Role')
