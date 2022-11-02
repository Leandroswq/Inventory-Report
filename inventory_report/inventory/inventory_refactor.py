from inventory_report.importer.importer import Importer
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path, _):
        data = self.importer.import_data(path)
        self.data.extend(data)

    def __iter__(self):
        return InventoryIterator(self.data)
