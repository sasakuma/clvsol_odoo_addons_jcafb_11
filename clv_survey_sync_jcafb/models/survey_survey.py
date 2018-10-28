# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SurveySurvey(models.Model):
    _name = 'survey.survey'
    _inherit = 'survey.survey', 'clv.abstract.external_sync'
