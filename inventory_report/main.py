import sys
import pathlib
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def get_importer(path):
    suffix = pathlib.Path(path).suffix

    if suffix == ".csv":
        return CsvImporter
    elif suffix == ".xml":
        return XmlImporter
    elif suffix == ".json":
        return JsonImporter
    else:
        raise ValueError(f"This function is incompatible with {suffix} files")


def get_report(data, type_report):
    if type_report == "simples":
        return SimpleReport.generate(list=data)
    elif type_report == "completo":
        return CompleteReport.generate(list=data)

    raise ValueError("Invalid type report")


def main():
    """_summary_

    Returns:
        _type_: _description_
    """
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    path = sys.argv[1]
    type_report = sys.argv[2]

    importer = get_importer(path)
    inventory = InventoryRefactor(importer)
    inventory.import_data(path)

    report = get_report(inventory.data, type_report)

    print(report, end="")
