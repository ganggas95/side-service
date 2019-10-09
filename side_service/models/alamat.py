from side_service import db


class Alamat(db.Model):
    __tablename__ = 'tb_alamat'
    id = db.Column(db.Integer, primary_key=True)
    kode_desa = db.Column(db.String(100))
    dusun = db.Column(db.String(200))
    rt_rw = db.Column(db.String(100))
    kode_pos = db.Column(db.String(5))

    @property
    def desa(self):
        # Return desa here 
        # Get desa from self.kode_desa
        return True

    @property
    def kecamatan(self):
        # Return kecamatan here 
        # Get kecamatan from kode_desa
        return True
    
    @property
    def kabupaten(self):
        # Return kabupaten here 
        # Get kabupaten from kecamatan
        return True
    
    @property
    def provinsi(self):
        # Return kabupaten here 
        # Get kabupaten from kecamatan
        return True
