#%%
import odoo
from odoo.tools import config
import base64
import io
from pandas import Series, DataFrame
import csv
import pandas as pd
import numpy as np
#%%
args = ['--log-level','debug']
odoo.cli.server.report_configuration()
#odoo.service.server.start(preload=[], stop=True)

local_vars = {
            'openerp': odoo,
            'odoo': odoo,
        }
context = odoo.api.Environment.manage()
v = context.__enter__()
dbname = 'erp'
if dbname:
    registry = odoo.registry(dbname)
    cr = registry.cursor().__enter__()
    uid = odoo.SUPERUSER_ID
    ctx = odoo.api.Environment(cr, uid, {})['res.users'].context_get()
    env = odoo.api.Environment(cr, uid, ctx)
    local_vars['env'] = env
    local_vars['self'] = env.user
    cr.rollback()
else:
    self.console(local_vars)

#%%
env['ir.ui.view'].with_context({'lang':'zh_CN'}).browse(1951).arch_db

#%%
self = env.user
Attach = self.env['ir.attachment']
ids = Attach.search([('datas_fname', 'like', '%.xls')])
ids
ata = ids[0]
#%%
ff = io.BytesIO(base64.b64decode(ata.datas))
df = pd.read_excel(ff)
df

#%%
cr.__exit__(None, None, None);
context.__exit__(None, None, None)
exit()