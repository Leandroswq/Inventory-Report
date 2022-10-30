import pathlib
import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        suffix = pathlib.Path(path).suffix

        if suffix != ".csv":
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            header, *data = csv_reader

        inventory_list = [
            {header[i]: inventory[i] for i in range(len(header))}
            for inventory in data
        ]

        return inventory_list

