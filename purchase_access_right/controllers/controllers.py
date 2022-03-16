# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseAccessRight(http.Controller):
#     @http.route('/purchase_access_right/purchase_access_right', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_access_right/purchase_access_right/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_access_right.listing', {
#             'root': '/purchase_access_right/purchase_access_right',
#             'objects': http.request.env['purchase_access_right.purchase_access_right'].search([]),
#         })

#     @http.route('/purchase_access_right/purchase_access_right/objects/<model("purchase_access_right.purchase_access_right"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_access_right.object', {
#             'object': obj
#         })
