from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from . import db, BaseModel


class Alamat(db.Model, BaseModel):
    __tablename__ = 'tb_alamat'
    id = db.Column(db.Integer, primary_key=True)
    kode_desa = db.Column(db.String(100), ForeignKey("tb_desa.kode_desa"))
    dusun = db.Column(db.String(200))
    rt_rw = db.Column(db.String(100))
    kode_pos = db.Column(db.String(5))
    desa = relationship("Desa", backref="desa")

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
