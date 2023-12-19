import psycopg2
from psycopg2 import sql
from odoo import models, fields, api
from itertools import cycle

class ManageMahasiswa(models.Model):
    
    @staticmethod
    def get_db_connection():
        return psycopg2.connect(
            dbname="praktikum_psd",
            user="openpg",
            password="openpgpwd",
            host="localhost",
            port="5432",
        )

    @staticmethod
    def get_cursor(connection):
        return connection.cursor()
    
    _name = 'manage.mahasiswa'
    _description = 'Manage Mahasiswa'

    ref = fields.Char(string='NIM')
    name = fields.Char(string='Name')
    average = fields.Float(string='Average', compute='calculateAvg', store=True)
    cluster = fields.Integer(string='Cluster')
    semester = fields.Integer(string='Semester') 

    pancasila = fields.Float(string='Pancasila')
    teknikDokumentasi = fields.Float(string='Teknik Dokumentasi')
    ilmuKomunikasidanOrganisasi = fields.Float(string='Ilmu Komunikasi dan Organisasi')
    aplikasiKomputerPerkantoran = fields.Float(string='Aplikasi Komputer Perkantoran')
    bahasaInggris = fields.Float(string='Bahasa Inggris')
    konsepTeknologiInformasi = fields.Float(string='Konsep Teknologi Informasi')
    matematikaDiskrit = fields.Float(string='Matematika Diskrit')
    keselamatandanKesehatanKerja = fields.Float(string='Keselamatan Kesehatan Kerja')
    dasarPemrograman = fields.Float(string='Dasar Pemrograman')
    praktikumDasarPemrograman = fields.Float(string='Praktikum Dasar Pemrograman')
    agama = fields.Float(string='Agama')
    kewarganegaraan = fields.Float(string='Kewarganegaraan')
    penulisanIlmiah = fields.Float(string='Penulisan Ilmiah')
    sistemOperasi = fields.Float(string='Sistem Operasi')
    pengembanganPerangkatLunakBerbasisObjek = fields.Float(string='Pengembangan Perangkat Lunak Berbasis Objek')
    desaindanPemrogramanWeb = fields.Float(string='Desain dan Pemrograman Web')
    basisData = fields.Float(string='Basis Data')
    praktikumBasisData = fields.Float(string='Praktikum Basis Data')
    strukturData = fields.Float(string='Struktur Data')
    praktikumStrukturData = fields.Float(string='Praktikum Struktur Data')
    interaksiManusiaKomputer = fields.Float(string='Interaksi Manusia Komputer')
    analisisdanPerancanganSistemInformasi = fields.Float(string='Analisis dan Perancangan Sistem Informasi')
    basisDataLanjut = fields.Float(string='Basis Data Lanjut')
    praktikumBasisDataLanjut = fields.Float(string='Praktikum Basis Data Lanjut')
    pemrogramanBerbasisObjek = fields.Float(string='Pemrograman Berbasis Objek')
    praktikumPemrogramanBerbasisObjek = fields.Float(string='Praktikum Pemrograman Berbasis Objek')
    statistika = fields.Float(string='Statistika')
    jaringanKomputer = fields.Float(string='Jaringan Komputer')
    praktikumJaringanKomputer = fields.Float(string='Praktikum Jaringan Komputer')
    manajemenProyekSistemInformasi = fields.Float(string='Manajemen Proyek Sistem Informasi')
    analisisProsesBisnis = fields.Float(string='Analisis Proses Bisnis')
    pengenalanSistemInformasi = fields.Float(string='Pengenalan Sistem Informasi')
    rekayasaPerangkatLunak = fields.Float(string='Rekayasa Perangkat Lunak')
    eBusiness = fields.Float(string='E-Business')
    dataWarhouse = fields.Float(string='Data Warehouse')
    workshop1 = fields.Float(string='Workshop 1')
    pengantarAkuntasiManajemendanBisnis = fields.Float(string='Pengantar Akuntasi Manajemen dan Bisnis')
    
    @api.model
    def create_record(self, values):
        # Gunakan method create untuk membuat rekaman baru berdasarkan values yang diterima
        new_record = self.create(values)
        return new_record

    @api.depends("pancasila", "teknikDokumentasi", "ilmuKomunikasidanOrganisasi", "aplikasiKomputerPerkantoran", "bahasaInggris", "konsepTeknologiInformasi", "matematikaDiskrit", "keselamatandanKesehatanKerja", "dasarPemrograman", "praktikumDasarPemrograman", "agama", "kewarganegaraan", "penulisanIlmiah", "sistemOperasi", "pengembanganPerangkatLunakBerbasisObjek", "desaindanPemrogramanWeb", "basisData", "praktikumBasisData", "strukturData", "praktikumStrukturData", "interaksiManusiaKomputer", "analisisdanPerancanganSistemInformasi", "basisDataLanjut", "praktikumBasisDataLanjut", "pemrogramanBerbasisObjek", "praktikumPemrogramanBerbasisObjek", "statistika", "jaringanKomputer", "praktikumJaringanKomputer", "manajemenProyekSistemInformasi", "analisisProsesBisnis","pengenalanSistemInformasi","rekayasaPerangkatLunak", "eBusiness", "dataWarhouse", "workshop1", "pengantarAkuntasiManajemendanBisnis")
    def calculateAvg(self):
        for record in self:
            total = record.pancasila + record.teknikDokumentasi + record.ilmuKomunikasidanOrganisasi + record.aplikasiKomputerPerkantoran + record.bahasaInggris + record.konsepTeknologiInformasi + record.matematikaDiskrit + record.keselamatandanKesehatanKerja + record.dasarPemrograman + record.praktikumDasarPemrograman + record.agama + record.kewarganegaraan + record.penulisanIlmiah + record.sistemOperasi + record.pengembanganPerangkatLunakBerbasisObjek + record.desaindanPemrogramanWeb + record.basisData + record.praktikumBasisData + record.strukturData + record.praktikumStrukturData + record.interaksiManusiaKomputer + record.analisisdanPerancanganSistemInformasi + record.basisDataLanjut + record.praktikumBasisDataLanjut + record.pemrogramanBerbasisObjek + record.praktikumPemrogramanBerbasisObjek + record.statistika + record.jaringanKomputer + record.praktikumJaringanKomputer + record.manajemenProyekSistemInformasi + record.analisisProsesBisnis + record.pengenalanSistemInformasi + record.rekayasaPerangkatLunak + record.eBusiness + record.dataWarhouse + record.workshop1 + record.pengantarAkuntasiManajemendanBisnis
            record.average = total / 37
        
    @api.depends('average')
    def calculate_cluster(self):
        for record in self:
            if record.average:
                low_boundary = record.search([], order='average', limit=1).average
                high_boundary = record.search([], order='average desc', limit=1).average
                range_size = (high_boundary - low_boundary) / 3

                if record.average <= low_boundary + range_size:
                    record.cluster = 1
                elif low_boundary + range_size < record.average <= low_boundary + 2 * range_size:
                    record.cluster = 2
                else:
                    record.cluster = 3

    def button_calculate_cluster(self):
        self.calculate_cluster()
    
    @api.model
    def distribute_students(self):
        student_class_pairs = []  # Array untuk menampung pasangan id mahasiswa dan id kelas

        with ManageMahasiswa.get_db_connection() as connection:
            cursor = ManageMahasiswa.get_cursor(connection)

            try:
                # Mendapatkan jumlah kelas
                cursor.execute("SELECT id, name_class FROM edumixr_classroom;")
                classrooms = cursor.fetchall()

                if not classrooms:
                    raise ValueError("Tidak ada kelas yang tersedia untuk mendistribuskan mahasiswa.")

                # Mendapatkan jumlah mahasiswa berdasarkan cluster
                cursor.execute("SELECT cluster, COUNT(*) FROM manage_mahasiswa GROUP BY cluster ORDER BY cluster;")
                cluster_counts = dict(cursor.fetchall())

                # Pastikan jumlah mahasiswa cukup untuk pembagian rata ke dalam kelas
                min_students_per_class = min(cluster_counts.values())
                if min_students_per_class * len(classrooms) > sum(cluster_counts.values()):
                    raise ValueError("Jumlah mahasiswa tidak cukup untuk pembagian rata ke dalam kelas.")

                # Mendapatkan id mahasiswa berdasarkan cluster
                cursor.execute("SELECT id, cluster FROM manage_mahasiswa ORDER BY cluster;")
                students = cursor.fetchall()
                
                classrooms_cycle = cycle(classrooms)

                # Distribusi mahasiswa ke dalam kelas secara merata
                for student in students:
                    student_id, cluster = student
                    
                    classroom_id = next(classrooms_cycle)[0]
                    student_class_pairs.append({"student_id": student_id, "classroom_id": classroom_id})

                    cursor.execute(
                        "INSERT INTO edumixr_classroom_manage_mahasiswa_rel (edumixr_classroom_id, manage_mahasiswa_id) "
                        "VALUES (%s, %s);",
                        (classroom_id, student_id)
                    )
                    
                # Commit perubahan
                connection.commit()

            except Exception as e:
                # Handle exception
                connection.rollback()  # Rollback perubahan jika terjadi kesalahan
                raise e

            finally:
                connection.close()

        return student_class_pairs  # Mengembalikan array pasangan id mahasiswa dan id kelas

    @api.model
    def run_clustering(self):
        manage_mahasiswa = self.env['manage.mahasiswa'].search([])
        manage_mahasiswa.button_calculate_cluster()

    

