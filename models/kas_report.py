from odoo import models, fields, api

class KasReport(models.Model):
    _name = 'kas.report'

    name = fields.Char(string='Name')
    total_pinjaman = fields.Float(string='Total Pinjaman', compute='get_pinjaman_total')

    @api.one
    def get_pinjaman_total(self):
        # total_pinjaman = []
        # domain = [('total_angsuran','not in',[False,None])]
        # for rec in self.env['ksp.kredit'].search(domain):
        #     if rec.total_angsuran: 
        #         self.total_pinjaman = sum(total_pinjaman.append(self.total_angsuran)) 
        # self.total_pinjaman += self.env['ksp.kredit'].total_angsuran
        # temp_array = []
        # temp_array = self.env['ksp.kredit'].search([('total_angsuran','not in',[False,None])]).mapped('total_angsuran')
        # equal to ~
        # for doc in docs:
        #     self.total_pinjaman = sum(temp_array.append(doc.total_angsuran))
        docs = self.env['ksp.kredit'].search([('total_angsuran','not in',[False,None])])
        self.total_pinjaman = sum(doc.total_angsuran for doc in docs)
        return