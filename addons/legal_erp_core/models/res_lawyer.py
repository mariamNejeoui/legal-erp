from odoo import models, fields

class ResLawyer(models.Model):
    _inherit = 'res.users'

    # --- Custom Fields from ER Diagram ---
    
    bar_number = fields.Char(string='Bar Number')
    
    specialization = fields.Selection([
        ('civil', 'Civil Law'),
        ('criminal', 'Criminal Law'),
        ('labor', 'Labor Law'),
        ('commercial', 'Commercial Law'),
        ('tax', 'Tax Law')
    ], string='Specialization')
    
    role_level = fields.Selection([
        ('junior', 'Junior Associate'),
        ('mid', 'Mid-level Associate'),
        ('senior', 'Senior Associate'),
        ('partner', 'Partner')
    ], string='Role Level')

    internal_hourly_rate = fields.Float(string='Internal Hourly Rate')
    billing_hourly_rate = fields.Float(string='Billing Hourly Rate')
    
    # Hemos omitido first_name, last_name, work_email e is_active 
    # porque Odoo ya los gestiona internamente con sus campos 'name', 'login' y 'active'.