from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import SimpleReport

DICT = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-06",
        "data_de_validade": "2023-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
    {
        "id": "3",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-03-18",
        "data_de_validade": "2023-10-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
]


def set_color(text: str, color: str):
    if color == "blue":
        color_code = 36
    if color == "green":
        color_code = 32
    if color == "red":
        color_code = 31
    return f"\33[{color_code}m{text}\033[0m"


green = [
    set_color("Data de fabricação mais antiga:", "green"),
    set_color("Data de validade mais próxima:", "green"),
    set_color("Empresa com mais produtos:", "green"),
]

blue = [set_color("2020-12-06", "blue"), set_color("2023-09-17", "blue")]

red = [set_color("Target Corporation", "red")]


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)
    report = colored_report.generate(DICT)

    report_validate = (
        f"{green[0]} {blue[0]}\n"
        f"{green[1]} {blue[1]}\n"
        f"{green[2]} {red[0]}"
    )

    assert report_validate == report
