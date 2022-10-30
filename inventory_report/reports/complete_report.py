from inventory_report.reports.simple_report import SimpleReport
from typing import List, Dict


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list: List[Dict[str, str]]) -> str:
        simple_report = SimpleReport.generate(list=list)
        companies = CompleteReport._total_product_by_company(list=list)

        companies_total_products_report = ""

        for company in companies:
            companies_total_products_report += (
                f"- {company}: {companies[company]['total']}\n"
            )

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_total_products_report}"
        )
