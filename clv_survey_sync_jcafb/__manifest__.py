# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Survey External Sync (for CLVhealth-JCAFB Solution)',
    'summary': 'Survey External Sync Module used in CLVhealth-JCAFB Solution.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_survey',
        'clv_external_sync',
    ],
    'data': [
        'views/survey_survey_view.xml',
        # 'views/survey_page_view.xml',
        # 'views/survey_question_view.xml',
        # 'views/survey_label_view.xml',
        # 'views/survey_user_input_view.xml',
        'data/survey_stage.xml',
        'data/survey_survey.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
