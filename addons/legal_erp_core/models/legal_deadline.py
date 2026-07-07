from odoo import models, fields

class LegalDeadline(models.Model):
    _name = 'legal.deadline'
    _description = 'Legal Deadline'

    # --- Basic Fields ---
    description = fields.Char(string='Description', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    
    # Selection fields (replacing the Int types from the diagram)
    deadline_type = fields.Selection([
        ('court', 'Court / Judicial'),
        ('administrative', 'Administrative'),
        ('internal', 'Internal')
    ], string='Deadline Type', required=True)
    
    status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Completed'),
        ('overdue', 'Overdue')
    ], string='Status', default='pending')

    # --- Booleans ---
    is_alert_sent = fields.Boolean(string='Alert Sent', default=False)
    is_confidential = fields.Boolean(string='Confidential', default=False)

    # --- FOREIGN KEYS (Relations) ---
    
    # FK: case_id -> Conecta con el modelo de expediente que creamos antes
    case_id = fields.Many2one(
        'legal.case', 
        string='Legal Case', 
        required=True, 
        ondelete='cascade' # Si borras el expediente, se borran sus plazos automáticamente
    )
    
    # FK: assigned_lawyer_id -> Conecta con el abogado encargado (usuario de Odoo)
    assigned_lawyer_id = fields.Many2one(
        'res.users', 
        string='Assigned Lawyer', 
        ondelete='set null'
    )