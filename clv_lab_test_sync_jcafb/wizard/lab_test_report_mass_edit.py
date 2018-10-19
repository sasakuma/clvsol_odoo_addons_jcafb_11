# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestReportMassEdit(models.TransientModel):
    _inherit = 'clv.lab_test.report.mass_edit'

    external_sync = fields.Selection(
        [('included', 'Included'),
         ('updated', 'Updated'),
         ('synchronized', 'Synchronized'),
         ('missing', 'Missing'),
         ], 'External Synchronization'
    )
    external_sync_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='External Synchronization', default=False, readonly=False, required=False
    )

    @api.multi
    def do_lab_test_report_mass_edit(self):
        self.ensure_one()

        super(LabTestReportMassEdit, self).do_lab_test_report_mass_edit()

        for lab_test_report in self.lab_test_report_ids:

            _logger.info(u'%s %s', '>>>>>', lab_test_report.code)

            if self.external_sync_selection == 'set':
                lab_test_report.external_sync = self.external_sync
            if self.external_sync_selection == 'remove':
                lab_test_report.external_sync = False

        return True
