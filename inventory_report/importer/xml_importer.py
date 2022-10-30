import pathlib
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        suffix = pathlib.Path(path).suffix

        if suffix != ".xml":
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            content = file.read()
        data = xmltodict.parse(content)["dataset"]["record"]

        return data
