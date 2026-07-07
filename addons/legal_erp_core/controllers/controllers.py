# from odoo import http


# class LegalErpCore(http.Controller):
#     @http.route('/legal_erp_core/legal_erp_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/legal_erp_core/legal_erp_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('legal_erp_core.listing', {
#             'root': '/legal_erp_core/legal_erp_core',
#             'objects': http.request.env['legal_erp_core.legal_erp_core'].search([]),
#         })

#     @http.route('/legal_erp_core/legal_erp_core/objects/<model("legal_erp_core.legal_erp_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('legal_erp_core.object', {
#             'object': obj
#         })

