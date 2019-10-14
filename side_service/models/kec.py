from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from . import BaseModel, db


class Kecamatan(db.Model, BaseModel):
    __tablename__ = "tb_kec"

    kode_kec = Column(String(40), unique=True,
                       autoincrement=False, primary_key=True)
    name = Column(String(200))
    kode_kab = Column(String(100), ForeignKey("tb_kab.kode_kab"))
    kabupaten = relationship("Kabupaten", backref="kecamatan", foreign_keys=[kode_kab])
    list_desa = relationship("Desa", back_populates="kecamatan")

    def __init__(self, kode_kec: str, name: str, kode_kab: str):
        super(Kecamatan, self).__init__()
        self.name = name
        self.kode_kec = kode_kec
        self.kode_kab = kode_kab

    @staticmethod
    def all() -> list:
        return Kecamatan.query.all()

    @staticmethod
    def get_by_kode(kode_kec: str) -> object:
        return Kecamatan.query.filter(
            Kecamatan.kode_kec == kode_kec,
        ).first()

    @staticmethod
    def by_kode_kab(kode_kab: str):
        return Kecamatan.query.filter(
            Kecamatan.kode_kab == kode_kab
        ).all()
