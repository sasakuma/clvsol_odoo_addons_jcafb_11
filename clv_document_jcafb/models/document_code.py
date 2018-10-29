# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Document(models.Model):
    _name = "clv.document"
    _inherit = 'clv.document', 'clv.code.model'

    code = fields.Char(string='Document Code', required=False, default='/')
    code_sequence = fields.Char(default='clv.document.code')
