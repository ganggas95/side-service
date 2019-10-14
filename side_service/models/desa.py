from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from . import BaseModel, db


class Desa(db.Model, BaseModel):
    __tablename__ = "tb_desa"

    kode_desa = Column(String(40), unique=True,
                       autoincrement=False, primary_key=True)
    name = Column(String(200))
    kode_kec = Column(String(100), ForeignKey("tb_kec.kode_kec"))
    kecamatan = relationship("Kecamatan", backref="desa", foreign_keys=[kode_kec])

    def __init__(self, kode_desa: str, name: str, kode_kec: str):
        super(Desa, self).__init__()
        self.name = name
        self.kode_desa = kode_desa
        self.kode_kec = kode_kec

    @staticmethod
    def all() -> list:
        return Desa.query.all()

    @staticmethod
    def get_by_kode(kode_desa: str) -> object:
        return Desa.query.filter(
            Desa.kode_desa == kode_desa,
        ).first()

    @staticmethod
    def by_kode_kec(kode_kec: str):
        return Desa.query.filter(
            Desa.kode_kec == kode_kec,
        ).all()
