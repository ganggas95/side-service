import os
from numpy import int64
import pandas as pd
from flask import current_app as app
from side_service.models.prov import Provinsi
from side_service.models.kab import Kabupaten
from side_service.models.kec import Kecamatan
from side_service.models.desa import Desa


class FileImporter:
    temps = []

    def __init__(self, filename):
        if filename:
            self.df = pd.read_csv(os.path.join(
                app.config["FILE_IMPORT_FOLDER"],
                filename), header=None)


class ImportProvinceFile(FileImporter):
    def read_data(self):
        for row in range(0, len(self.df.index)):
            kode_prov = str(self.df[0][self.df.index[row]])
            name = self.df[1][self.df.index[row]]
            prov = Provinsi(kode_prov, name)
            prov.save()
        print("Import Province is success")


class ImportRegenciesFile(FileImporter):

    @property
    def provs(self):
        return Provinsi.all()

    def read_data(self):
        for prov in self.provs:
            df_prov = self.df.loc[self.df[1] == int64(prov.kode_prov)]
            for row in range(0, len(df_prov.index)):
                kode_kab = str(df_prov[0][df_prov.index[row]])
                name = df_prov[2][df_prov.index[row]]
                kab = Kabupaten(kode_kab, name, prov.kode_prov)
                kab.save()
        print("Import Kabupaten is success")


class ImportDistrictFile(FileImporter):

    @property
    def kabs(self):
        return Kabupaten.all()

    def read_data(self):
        for kab in self.kabs:
            df_kab = self.df.loc[self.df[1] == int64(kab.kode_kab)]
            for row in range(0, len(df_kab.index)):
                kode_kec = str(df_kab[0][df_kab.index[row]])
                name = df_kab[2][df_kab.index[row]]
                kec = Kecamatan(kode_kec, name, kab.kode_kab)
                kec.save()
        print("Import District Success")


class ImportVillagesFile(FileImporter):
    @property
    def kecs(self):
        return Kecamatan.all()

    def read_data(self):
        for kec in self.kecs:
            df_desa = self.df.loc[self.df[1] == int64(kec.kode_kec)]
            for row in range(0, len(df_desa.index)):
                kode_desa = str(df_desa[0][df_desa.index[row]])
                name = df_desa[2][df_desa.index[row]]
                desa = Desa(kode_desa, name, kec.kode_kec)
                desa.save()
        print("Import Villages Success")
