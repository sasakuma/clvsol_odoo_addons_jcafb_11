# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Lab Test External Sync (for CLVhealth-JCAFB Solution)',
    'summary': 'Lab Test External Sync Module used in CLVhealth-JCAFB Solution.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_lab_test',
        'clv_external_sync',
    ],
    'data': [
        'views/lab_test_unit_view.xml',
        'views/lab_test_type_view.xml',
        'views/lab_test_request_view.xml',
        'views/lab_test_result_view.xml',
        'views/lab_test_report_view.xml',
        'views/lab_test_criterion_view.xml',
        'wizard/lab_test_request_mass_edit_view.xml',
        'wizard/lab_test_result_mass_edit_view.xml',
        'wizard/lab_test_report_mass_edit_view.xml',
        'data/external_sync.xml',
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
