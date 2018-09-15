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

# from odoo import api, fields, models
from odoo import api, fields, models


class Animal(models.Model):
    _inherit = 'clv.animal'

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


class Animal_2(models.Model):
    _inherit = 'clv.animal'

    lab_test_request_ids = fields.One2many(
        string='Lab Test Requests',
        comodel_name='clv.lab_test.request',
        compute='_compute_lab_test_request_ids_and_count',
    )
    count_lab_test_requests = fields.Integer(
        compute='_compute_lab_test_request_ids_and_count',
    )

    @api.multi
    def _compute_lab_test_request_ids_and_count(self):
        for record in self:
            lab_test_requests = self.env['clv.lab_test.request'].search([
                ('ref_id', '=', self._name + ',' + str(record.id)),
            ])
            record.count_lab_test_requests = len(lab_test_requests)
            record.lab_test.request_ids = [(6, 0, lab_test_requests.ids)]


class Animal_3(models.Model):
    _inherit = 'clv.animal'

    lab_test_result_ids = fields.One2many(
        string='Lab Test Results',
        comodel_name='clv.lab_test.result',
        compute='_compute_lab_test_result_ids_and_count',
    )
    count_lab_test_results = fields.Integer(
        compute='_compute_lab_test_result_ids_and_count',
    )

    @api.multi
    def _compute_lab_test_result_ids_and_count(self):
        for record in self:
            lab_test_results = self.env['clv.lab_test.result'].search([
                ('ref_id', '=', self._name + ',' + str(record.id)),
            ])
            record.count_lab_test_results = len(lab_test_results)
            record.lab_test.result_ids = [(6, 0, lab_test_results.ids)]


class Animal_4(models.Model):
    _inherit = 'clv.animal'

    lab_test_report_ids = fields.One2many(
        string='Lab Test Reports',
        comodel_name='clv.lab_test.report',
        compute='_compute_lab_test_report_ids_and_count',
    )
    count_lab_test_reports = fields.Integer(
        compute='_compute_lab_test_report_ids_and_count',
    )

    @api.multi
    def _compute_lab_test_report_ids_and_count(self):
        for record in self:
            lab_test_reports = self.env['clv.lab_test.report'].search([
                ('ref_id', '=', self._name + ',' + str(record.id)),
            ])
            record.count_lab_test_reports = len(lab_test_reports)
            record.lab_test.report_ids = [(6, 0, lab_test_reports.ids)]
