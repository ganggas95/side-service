from side_service import db


class Keluarga(db.Model):
    __tablename__ = 'tb_kk'
    id = db.Column(db.Integer, primary_key=True)
    no_kk = db.Column(db.String(100), unique=True)
    # Related to Alamat
    # TODO: create property to handle relationship
    alamat_id = db.Column(db.Integer)
    # Related to Penduduk
    kk_id = db.Column(db.Integer)
    # TODO: create property to handle relationship kepala_keluarga
