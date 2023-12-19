from odoo import fields, models

class matakuliah(models.Model):
    _name = "edumixr.matakuliah"
    _description = 'Manajemen Matakuliah'
    
    ref = fields.Char(
        string='Reference',
        required=True
    )
    matakuliah = fields.Char(
        string='Matakuliah',
        help="Masukkan matakuliah..."
    )
    sks  = fields.Integer(
        string='SKS',
        help='Masukkan SKS...'
    )
    pengampu_id = fields.Many2one(
        'edumixr.dosen', #ambil ref dosen
        string='Dosen Pengampu'
    )