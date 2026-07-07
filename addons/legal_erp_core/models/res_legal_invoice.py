from odoo import models, fields

class ResLegalInvoice(models.Model):
    _inherit = 'account.move'

    # --- CUSTOM FOREIGN KEYS FROM ER DIAGRAM ---
    
    # FK: case_id -> Conectado al expediente para saber a qué caso pertenece la factura
    case_id = fields.Many2one(
        'legal.case', 
        string='Legal Case', 
        ondelete='set null'
    )
    
    # FK: agreement_id -> Conectado al acuerdo de honorarios que originó esta factura
    agreement_id = fields.Many2one(
        'legal.fee.agreement', 
        string='Fee Agreement', 
        ondelete='set null'
    )