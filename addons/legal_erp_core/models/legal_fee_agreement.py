from odoo import models, fields

class LegalFeeAgreement(models.Model):
    _name = 'legal.fee.agreement'
    _description = 'Fee Agreement'

    # --- Basic Fields ---
    # Añadimos un campo 'name' para que Odoo tenga un título que mostrar en los desplegables
    name = fields.Char(string='Agreement Reference', required=True, help="e.g., AGR-2026-001")
    
    # Transformamos el Int del diagrama en un desplegable claro
    billing_model = fields.Selection([
        ('hourly', 'Hourly Rate (Por Horas)'),
        ('fixed', 'Fixed Fee (Precio Cerrado)'),
        ('retainer', 'Retainer / Mixed (Provisión / Mixto)')
    ], string='Billing Model', required=True)

    # Los campos Double pasan a Float
    hourly_rate = fields.Float(string='Hourly Rate')
    fixed_amount = fields.Float(string='Fixed Amount')
    retainer_fee = fields.Float(string='Retainer Fee (Provisión)')
    
    is_retainer_paid = fields.Boolean(string='Is Retainer Paid', default=False)

    # --- FOREIGN KEYS (Relations) ---
    
    # FK: client_id -> Conectado al cliente (res.partner)
    client_id = fields.Many2one(
        'res.partner', 
        string='Client', 
        required=True, 
        ondelete='restrict' # No permitimos borrar al cliente si tiene acuerdos económicos activos
    )