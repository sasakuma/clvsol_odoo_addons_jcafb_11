# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestReport(models.Model):
    _name = 'clv.lab_test.report'
    _inherit = 'clv.lab_test.report', 'clv.abstract.external_sync'
