# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestRequest(models.Model):
    _name = 'clv.lab_test.request'
    _inherit = 'clv.lab_test.request', 'clv.abstract.external_sync'
