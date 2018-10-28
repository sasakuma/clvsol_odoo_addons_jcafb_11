# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SurveyStage(models.Model):
    _name = 'survey.stage'
    _inherit = 'survey.stage', 'clv.abstract.external_sync'
