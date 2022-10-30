import pathlib
import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        suffix = pathlib.Path(path).suffix

        if suffix != ".json":
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            content = file.read()
        data = json.loads(content)

        return data
