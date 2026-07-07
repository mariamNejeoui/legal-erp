from odoo import models, fields

class LegalDocument(models.Model):
    _name = 'legal.document'
    _description = 'Legal Document'

    # --- Basic Fields ---
    file_name = fields.Char(string='File Name', required=True)
    
    # Puede ser 'pdf', 'docx', 'jpg', etc.
    file_type = fields.Char(string='File Type') 
    
    # Aquí irá el enlace a AWS S3
    file_url = fields.Char(string='File URL', required=True)
    
    upload_date = fields.Date(string='Upload Date', default=fields.Date.context_today, required=True)
    is_confidential = fields.Boolean(string='Is Confidential', default=False)

    # --- FOREIGN KEYS (Relations) ---
    
    # FK: case_id -> Conectado al expediente
    case_id = fields.Many2one(
        'legal.case', 
        string='Legal Case', 
        ondelete='cascade' # Si se borra el caso, se borran sus documentos
    )
    
    # FK: client_id -> Conectado al cliente (res.partner)
    client_id = fields.Many2one(
        'res.partner', 
        string='Client', 
        ondelete='cascade'
    )
    
    # FK: uploaded_by_id -> Quién subió el archivo (res.users)
    uploaded_by_id = fields.Many2one(
        'res.users', 
        string='Uploaded By', 
        default=lambda self: self.env.user, # Por defecto, el usuario actual
        ondelete='restrict'
    )