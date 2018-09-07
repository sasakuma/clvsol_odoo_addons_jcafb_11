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
from odoo import fields, models


class Patient(models.Model):
    _inherit = 'clv.patient'

    patient_document_ids = fields.One2many(
        string='Documents',
        related='partner_id.document_ids',
        readonly=False
    )
    patient_count_documents = fields.Integer(
        string='Number of Documents',
        related='partner_id.count_documents',
        readonly=False
    )
    # document_ids = fields.One2many(
    #     comodel_name='clv.document',
    #     inverse_name='patient_id',
    #     string='Documents'
    # )
    # count_documents = fields.Integer(
    #     string='Number of Documents',
    #     compute='_compute_count_documents'
    # )

    # @api.depends('document_ids')
    # def _compute_count_documents(self):
    #     for r in self:
    #         r.count_documents = len(r.document_ids)


class Document(models.Model):
    _inherit = 'clv.document'

    # patient_id = fields.Many2one(
    #     comodel_name='clv.patient',
    #     string='Patient',
    #     ondelete='restrict'
    # )
    # patient_code = fields.Char(
    #     string='Patient Code',
    #     related='patient_id.code',
    #     readonly=True
    # )
    # patient_employee_id = fields.Many2one(
    #     comodel_name='hr.employee',
    #     string='Responsible Empĺoyee (Patient)',
    #     related='patient_id.address_id.employee_id',
    #     store=True
    # )
