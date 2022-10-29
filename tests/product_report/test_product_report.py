from inventory_report.inventory.product import Product
import datetime


def test_relatorio_produto():
    product_data = {
        "id": 0,
        "nome_do_produto": "Azeitona",
        "nome_da_empresa": "Empresa x",
        "data_de_fabricacao": datetime.datetime(2020, 5, 17),
        "data_de_validade": datetime.datetime(2020, 9, 17),
        "numero_de_serie": 0,
        "instrucoes_de_armazenamento": "Exemplo",
    }

    product = Product(
        id=product_data["id"],
        nome_do_produto=product_data["nome_do_produto"],
        nome_da_empresa=product_data["nome_da_empresa"],
        data_de_fabricacao=product_data["data_de_fabricacao"],
        data_de_validade=product_data["data_de_validade"],
        numero_de_serie=product_data["numero_de_serie"],
        instrucoes_de_armazenamento=product_data[
            "instrucoes_de_armazenamento"
        ],
    )

    aux_instrucoes = product_data["instrucoes_de_armazenamento"]

    product_repr = (
        f"O produto {product_data['nome_do_produto']}"
        f" fabricado em {product_data['data_de_fabricacao']}"
        f" por {product_data['nome_da_empresa']} com validade"
        f" até {product_data['data_de_validade']}"
        f" precisa ser armazenado {aux_instrucoes}."
    )

    assert repr(product) == product_repr
