from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from . import BaseModel, db


class Kabupaten(db.Model, BaseModel):
    __tablename__ = "tb_kab"

    kode_kab = Column(String(40), unique=True,
                       autoincrement=False, primary_key=True)
    name = Column(String(200))
    kode_prov = Column(String(100), ForeignKey("tb_prov.kode_prov"))
    provinsi = relationship("Provinsi", backref="kabupaten", foreign_keys=[kode_prov])
    list_kecamatan = relationship("Kecamatan", back_populates="kabupaten")

    def __init__(self, kode_kab: str, name: str, kode_prov: str):
        super(Kabupaten, self).__init__()
        self.name = name
        self.kode_kab = kode_kab
        self.kode_prov = kode_prov

    @staticmethod
    def all() -> list:
        return Kabupaten.query.all()

    @staticmethod
    def get_by_kode(kode_kab: str) -> object:
        return Kabupaten.query.filter(
            Kabupaten.kode_kab == kode_kab,
        ).first()

    @staticmethod
    def by_kode_prov(kode_prov: str):
        return Kabupaten.query.filter(
            Kabupaten.kode_prov == kode_prov
        ).all()
