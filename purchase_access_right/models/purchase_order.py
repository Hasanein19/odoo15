# Copyright 2018-2019 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

from odoo import _, api, exceptions, fields, models
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('first_approval', 'First approval'),
        ('second_approval', 'Second approval'),
        ('purchase', 'Confirm Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, index=True, copy=False, default='draft', track_visibility='onchange')

    def move_to_first_approval(self):
        self.write({'state': 'first_approval'})

    def move_to_second_approval(self):
        self.write({'state': 'second_approval'})

    def button_confirm(self):
        for line in self:
            if line.amount_total == 0.0:
                raise ValidationError(
                    'Can not confirm Purchase Order with Amount Total equal Zero.')
        for order in self:
            if order.state not in ['draft', 'sent', 'second_approval']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step' \
                    or (order.company_id.po_double_validation == 'two_step' \
                        and order.amount_total < self.env.company.currency_id._convert(
                        order.company_id.po_double_validation_amount, order.currency_id, order.company_id,
                        order.date_order or fields.Date.today())) \
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
        return True

