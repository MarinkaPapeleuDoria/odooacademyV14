# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    """Add Customer comment functions to the website_sale controller."""
    @http.route(['/shop/customer_comment'], type='json', auth="public", methods=['POST'], website=True)
    def customer_comment(self, **post):
        """ Json method that used to add a
        comment when the user clicks on 'pay now' button.
        """

        if post.get('comment') or post.get('reference'):
            order = request.website.sale_get_order()
            redirection = self.checkout_redirection(order)

            if order and order.id:
                comment = 'No comment' if len(post.get('comment')) == 0 else post.get('comment')
                client_order_ref = 'No Reference' if len(post.get('reference')) == 0 else post.get('reference')
                order.write({'customer_comment': comment,
                             'client_order_ref': client_order_ref
                             })
            if redirection:
                return redirection

        return True
