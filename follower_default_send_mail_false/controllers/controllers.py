# -*- coding: utf-8 -*-
from odoo import http

# class FollowerDefaultSendMailFalse(http.Controller):
#     @http.route('/follower_default_send_mail_false/follower_default_send_mail_false/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/follower_default_send_mail_false/follower_default_send_mail_false/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('follower_default_send_mail_false.listing', {
#             'root': '/follower_default_send_mail_false/follower_default_send_mail_false',
#             'objects': http.request.env['follower_default_send_mail_false.follower_default_send_mail_false'].search([]),
#         })

#     @http.route('/follower_default_send_mail_false/follower_default_send_mail_false/objects/<model("follower_default_send_mail_false.follower_default_send_mail_false"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('follower_default_send_mail_false.object', {
#             'object': obj
#         })