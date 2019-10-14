from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from . import BaseModel, db


class Provinsi(db.Model, BaseModel):
    __tablename__ = "tb_prov"

    kode_prov = Column(String(40), unique=True,
                       autoincrement=False, primary_key=True)
    name = Column(String(200))
    list_kabupaten = relationship("Kabupaten", back_populates="provinsi")

    def __init__(self, kode_prov: str, name: str):
        super(Provinsi, self).__init__()
        self.name = name
        self.kode_prov = kode_prov

    @staticmethod
    def all() -> list:
        return Provinsi.query.all()

    @staticmethod
    def get_by_kode(kode_prov: str) -> object:
        return Provinsi.query.filter(
            Provinsi.kode_prov == kode_prov,
        ).first()
