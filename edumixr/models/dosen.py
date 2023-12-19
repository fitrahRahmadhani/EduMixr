from odoo import fields, models

class dosen(models.Model):
    _name = "edumixr.dosen"
    _description = 'Manajemen Dosen'
    
    ref = fields.Char(
        string='Reference',
        required=True
    )
    name = fields.Char(
        string='Nama Dosen',
        help="Masukkan nama dosen..."
        )
    nidn  = fields.Integer(
        string='NIDN',
        help='Masukkan NIDN...'
        )
    email = fields.Char(
        string='email',
        help="Masukkan email..."
        )