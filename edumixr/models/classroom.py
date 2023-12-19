from odoo import fields, models

class Classroom(models.Model):
    _name = "edumixr.classroom"
    _description = 'Manajemen Kelas'

    name_class = fields.Char(string='Nama Kelas', help="Masukkan nama kelas...")
    semester_class = fields.Integer(string='Semester', help='Masukkan semester...')
    dpa_id = fields.Many2one('edumixr.dosen', string='DPA')
    daftar_mahasiswa_ids = fields.Many2many('manage.mahasiswa', string='Mahasiswa Lines')
    matakuliah_ids = fields.Many2many('edumixr.matakuliah', string='Matakuliah Lines')
