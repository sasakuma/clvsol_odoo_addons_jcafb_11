# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import api, fields, models


class Patient(models.Model):
    _inherit = 'clv.patient'

    document_ids = fields.One2many(
        string='Documents',
        comodel_name='clv.document',
        compute='_compute_document_ids_and_count',
    )
    count_documents = fields.Integer(
        compute='_compute_document_ids_and_count',
    )

    @api.multi
    def _compute_document_ids_and_count(self):
        for record in self:
            documents = self.env['clv.document'].search([
                ('ref_id', '=', self._name + ',' + str(record.id)),
            ])
            record.count_documents = len(documents)
            record.document_ids = [(6, 0, documents.ids)]
