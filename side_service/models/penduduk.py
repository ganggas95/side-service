from side_service import db


class Penduduk(db.Model):
    __tablename__ = 'tb_penduduk'
    id = db.Column(db.Integer, primary_key=True)
    nik = db.Column(db.String(16), unique=True)
    nama = db.Column(db.String(400))
    jenis_kelamin = db.Column(db.String(100))
    tempat_lahir = db.Column(db.String(400))
    tanggal_lahir = db.Column(db.Date, default=None)
    golongan_darah = db.Column(db.String(40), default="-")
    agama = db.Column(db.String(100))
    pendidikan = db.Column(db.String(200))
    pekerjaan = db.Column(db.String(200))
    ayah = db.Column(db.Integer)
    ibu = db.Column(db.Integer)
    status_perkawinan = db.Column(db.String(200))
    status_wni = db.Column(db.Boolean, default=True)
    no_pasport = db.Column(db.String(200))
    no_kita = db.Column(db.String(200))
