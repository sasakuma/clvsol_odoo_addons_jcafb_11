# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SurveyLabel(models.Model):
    _name = 'survey.label'
    _inherit = 'survey.label', 'clv.abstract.external_sync'
