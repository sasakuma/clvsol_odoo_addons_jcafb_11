# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class Person(models.Model):
    _inherit = 'clv.person'

    @api.multi
    def _compute_document_ids_and_count(self):
        for record in self:

            search_domain = [
                ('ref_id', '=', self._name + ',' + str(record.id)),
            ]
            if record.phase_id.id is not False:
                search_domain.append(
                    ('phase_id.id', '=', record.phase_id.id),
                )

            documents = self.env['clv.document'].search(search_domain)

            record.count_documents = len(documents)
            record.document_ids = [(6, 0, documents.ids)]
