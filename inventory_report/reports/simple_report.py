from typing import List, Dict
from datetime import datetime
from copy import deepcopy


class SimpleReport:
    @staticmethod
    def _get_oldest_item(list: List[Dict[str, str]]):
        list_aux = deepcopy(list)
        list_aux.sort(
            key=lambda item: datetime.strptime(
                item["data_de_fabricacao"], "%Y-%m-%d"
            ),
            reverse=False,
        )
        return list_aux[0]

    @staticmethod
    def _get_closest_expiry_item(list: List[Dict[str, str]]):
        list_aux = deepcopy(list)

        list_aux.sort(
            key=lambda item: datetime.now()
            - datetime.strptime(item["data_de_validade"], "%Y-%m-%d"),
            reverse=True,
        )

        closest_expiry_item = [
            item
            for item in list_aux
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        ]

        return closest_expiry_item[0]

    @staticmethod
    def _total_product_by_company(list: List[Dict[str, str]]):
        companies = {}
        for item in list:
            company_name = item["nome_da_empresa"]
            if company_name in companies:
                companies[company_name]["total"] += 1
            else:
                companies[company_name] = {"total": 1, "name": company_name}

        return companies

    @staticmethod
    def _get_company_with_more_products(list: List[Dict[str, str]]):
        companies = SimpleReport._total_product_by_company(list=list)

        company_with_more_products = max(
            companies, key=lambda company: companies[company]["total"]
        )
        return company_with_more_products

    @staticmethod
    def generate(list: List[Dict[str, str]]) -> str:
        oldest = SimpleReport._get_oldest_item(list=list)
        closest_expiry_item = SimpleReport._get_closest_expiry_item(list=list)
        company_with_more_products = (
            SimpleReport._get_company_with_more_products(list=list)
        )
        closest_expiry_date = closest_expiry_item["data_de_validade"]
        return (
            f"Data de fabricação mais antiga: {oldest['data_de_fabricacao']}\n"
            f"Data de validade mais próxima: {closest_expiry_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
