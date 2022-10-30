import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


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
    def import_data(path: str, type: str):
        report_types = ["simples", "completo"]

        if type not in report_types:
            raise ValueError(
                "The parameter 'type' needs to be 'simples' or 'completo'"
            )

        inventory_list = Inventory.__load_data_csv__(path=path)

        if type == "simples":
            return SimpleReport.generate(list=inventory_list)
        elif type == "completo":
            return CompleteReport.generate(list=inventory_list)
