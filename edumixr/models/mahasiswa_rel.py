from odoo import models, fields

class ClassroomManageMahasiswaRel(models.Model):
    _name = 'edumixr.classroom.manage.mahasiswa.rel'
    _description = 'Mahasiswa Rel'

    edumixr_classroom_id = fields.Many2one('edumixr.classroom', string='Classroom')
    manage_mahasiswa_id = fields.Many2one('manage.mahasiswa', string='Manage Mahasiswa')