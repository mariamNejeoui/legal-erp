from odoo import models, fields

class LegalCase(models.Model):
    _name = 'legal.case'
    _description = 'Legal Case'

    # --- Basic Fields ---
    procedure_number = fields.Char(string='Procedure Number', required=True)
    title = fields.Char(string='Case Title', required=True)
    description = fields.Text(string='Description')
    
    # In Odoo, Ints representing statuses become 'Selection' fields
    status = fields.Selection([
        ('open', 'Open'),
        ('pending', 'Pending'),
        ('closed', 'Closed')
    ], string='Status', default='open')
    
    case_type = fields.Selection([
        ('civil', 'Civil'),
        ('criminal', 'Criminal'),
        ('labor', 'Labor'),
        ('commercial', 'Commercial')
    ], string='Case Type')

    # Dates and Strings
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    court = fields.Char(string='Court')

    # --- FOREIGN KEYS (Relations) ---
    
    # FK: client_id -> Connected to 'res.partner' (Odoo's native contact model)
    client_id = fields.Many2one(
        'res.partner', 
        string='Client', 
        required=True, 
        ondelete='restrict' # Prevents deleting a client if they have assigned cases.
    )
    
    # FK: lead_lawyer_id -> Connected to 'res.users' (Odoo's native user model)
    lead_lawyer_id = fields.Many2one(
        'res.users', 
        string='Lead Lawyer', 
        ondelete='set null'
    )
    
    # FK: agreement_id -> Connected to the fee agreement table we will create next
    agreement_id = fields.Many2one(
        'legal.fee.agreement', 
        string='Fee Agreement', 
        ondelete='set null'
    )