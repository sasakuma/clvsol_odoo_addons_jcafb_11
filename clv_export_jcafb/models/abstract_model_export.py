# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class AbstractModelExport(models.AbstractModel):
    _inherit = 'clv.abstract.model_export'

    def model_export_dir_path(self, export_type):
        if export_type == 'xls':
            return '/opt/odoo/filestore/jcafb/export/xls'
        if export_type == 'sqlite':
            return '/opt/odoo/filestore/jcafb/export/sqlite'
        return False
