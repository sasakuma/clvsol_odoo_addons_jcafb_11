# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SurveyPage(models.Model):
    _name = 'survey.page'
    _inherit = 'survey.page', 'clv.abstract.external_sync'
