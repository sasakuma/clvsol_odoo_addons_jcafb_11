# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Patient(models.Model):
    _inherit = 'clv.patient'

    event_ids = fields.One2many(
        string='Events',
        comodel_name='clv.event',
        compute='_compute_event_ids_and_count',
    )
    count_events = fields.Integer(
        compute='_compute_event_ids_and_count',
    )

    @api.multi
    def _compute_event_ids_and_count(self):
        for record in self:
            events = self.env['clv.event'].search([
                ('ref_id', '=', self._name + ',' + str(record.id)),
            ])
            record.count_events = len(events)
            record.event_ids = [(6, 0, events.ids)]
