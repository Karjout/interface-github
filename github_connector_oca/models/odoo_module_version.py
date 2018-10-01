# Copyright 2018 Road-Support - Roel Adriaans
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class OdooModuleVersion(models.Model):
    _inherit = 'odoo.module.version'

    _ODOO_DEVELOPMENT_STATUS_SELECTION = [
        ('Alpha', 'Alpha'),
        ('Beta', 'Beta'),
        ('Production/Stable', 'Production/Stable'),
        ('Mature', 'Mature'),
    ]

    development_status = fields.Selection(
        string='Module maturity',
        selection=_ODOO_DEVELOPMENT_STATUS_SELECTION,
        readonly=True,
    )

    @api.model
    def manifest_2_odoo(self, info, repository_branch, module):
        res = super(OdooModuleVersion, self).manifest_2_odoo(
            info, repository_branch, module
        )
        res['development_status'] = info.get('development_status', False)
        return res
