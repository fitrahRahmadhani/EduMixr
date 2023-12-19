import base64
import io
import pandas as pd
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ImportMahasiswaWizard(models.TransientModel):
    _name = 'edumixr.import.wizard'
    _description = 'Import Mahasiswa'

    file_name_import = fields.Char(string='File Name Import', invisible=True)
    file = fields.Binary(string='Select Excel File', required=True, help='Choose an Excel file')

    def import_excel_data(self):
        try:
            df = pd.read_excel(io.BytesIO(base64.b64decode(self.file)))

            for index, row in df.iterrows():
                values = {
                    'name': row['name'],
                    'ref': row['ref'], 
                    'semester': row['semester'], 
                    'pancasila': row['pancasila'],
                    'teknikDokumentasi': row['teknikDokumentasi'],
                    'ilmuKomunikasidanOrganisasi': row['ilmuKomunikasidanOrganisasi'],
                    'aplikasiKomputerPerkantoran': row['aplikasiKomputerPerkantoran'],
                    'bahasaInggris': row['bahasaInggris'],
                    'konsepTeknologiInformasi': row['konsepTeknologiInformasi'],
                    'matematikaDiskrit' : row['matematikaDiskrit'],
                    'keselamatandanKesehatanKerja' : row['keselamatandanKesehatanKerja'],
                    'dasarPemrograman': row['dasarPemrograman'],
                    'praktikumDasarPemrograman' : row['praktikumDasarPemrograman'],
                    'agama': row['agama'],
                    'kewarganegaraan': row['kewarganegaraan'],
                    'penulisanIlmiah': row['penulisanIlmiah'],
                    'sistemOperasi': row['sistemOperasi'],
                    'pengembanganPerangkatLunakBerbasisObjek': row['pengembanganPerangkatLunakBerbasisObjek'],
                    'desaindanPemrogramanWeb' : row['desaindanPemrogramanWeb'],
                    'basisData': row['basisData'],
                    'praktikumBasisData': row['praktikumBasisData'],
                    'strukturData': row['strukturData'],
                    'praktikumStrukturData' : row['praktikumStrukturData'],
                    'interaksiManusiaKomputer': row['interaksiManusiaKomputer'],
                    'analisisdanPerancanganSistemInformasi': row['analisisdanPerancanganSistemInformasi'],
                    'basisDataLanjut': row['basisDataLanjut'],
                    'praktikumBasisDataLanjut' : row['praktikumBasisDataLanjut'],
                    'pemrogramanBerbasisObjek' : row['pemrogramanBerbasisObjek'],
                    'praktikumPemrogramanBerbasisObjek': row['praktikumPemrogramanBerbasisObjek'],
                    'statistika': row['statistika'],
                    'jaringanKomputer': row['jaringanKomputer'],
                    'praktikumJaringanKomputer' : row['praktikumJaringanKomputer'],
                    'manajemenProyekSistemInformasi': row['manajemenProyekSistemInformasi'],
                    'analisisProsesBisnis': row['analisisProsesBisnis'],
                    'pengenalanSistemInformasi' : row['pengenalanSistemInformasi'],
                    'rekayasaPerangkatLunak': row['rekayasaPerangkatLunak'],
                    'eBusiness': row['eBusiness'],
                    'dataWarhouse' : row['dataWarhouse'],
                    'workshop1': row['workshop1'],
                    'pengantarAkuntasiManajemendanBisnis': row['pengantarAkuntasiManajemendanBisnis']
                }
                self.env['manage.mahasiswa'].create(values)

            return {'type': 'ir.actions.act_window_close'}

        except Exception as e:
            _logger.error(f"Error during import: {e}")
            return {'type': 'ir.actions.act_window_close', 'message': f"Error: {e}"}

