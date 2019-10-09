from side_service import db


class Desa(db.Model):
    __tablename__ = 'tb_desa'
    kode_desa = db.Column(db.String(20), primary_key=True, autoincrement=False)
    nama = db.Column(db.String(200))
    kode_kec = db.Column(db.String(200))


class Kecamatan(db.Model):
    __tablename__ = 'tb_kec'
    kode_kec = db.Column(db.String(20), primary_key=True, autoincrement=False)
    nama = db.Column(db.String(200))
    kode_kab = db.Column(db.String(200))


class Kabupaten(db.Model):
    __tablename__ = 'tb_kab'
    kode_kab = db.Column(db.String(20), primary_key=True, autoincrement=False)
    nama = db.Column(db.String(200))
    kode_prov = db.Column(db.String(200))


class Provinsi(db.Model):
    __tablename__ = 'tb_prov'
    kode_prov = db.Column(db.String(20), primary_key=True, autoincrement=False)
    nama = db.Column(db.String(200))
