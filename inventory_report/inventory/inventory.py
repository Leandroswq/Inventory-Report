import csv
import pathlib
from typing import Dict, List
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xmltodict


class Inventory:
    @staticmethod
    def __load_data_csv__(path: str):

        with open(path, "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            header, *data = csv_reader

        inventory_list = [
            {header[i]: inventory[i] for i in range(len(header))}
            for inventory in data
        ]

        return inventory_list

    @staticmethod
    def __load_data_xml__(path: str):
        with open(path, "r") as file:
            content = file.read()
        data = xmltodict.parse(content)["dataset"]["record"]

        return data

    @staticmethod
    def __generate_report__(data: List[Dict[str, str]], type: str):
        if type == "simples":
            return SimpleReport.generate(list=data)
        elif type == "completo":
            return CompleteReport.generate(list=data)

        raise ValueError("Invalid type report")

    @staticmethod
    def import_data(path: str, type: str):
        report_types = ["simples", "completo"]

        if type not in report_types:
            raise ValueError("Invalid type report")

        suffix = pathlib.Path(path).suffix

        if suffix == ".csv":
            inventory_list = Inventory.__load_data_csv__(path=path)
        elif suffix == ".xml":
            inventory_list = Inventory.__load_data_xml__(path=path)
        else:
            raise ValueError(
                f"This function is incompatible with {suffix} files"
            )

        return Inventory.__generate_report__(data=inventory_list, type=type)
