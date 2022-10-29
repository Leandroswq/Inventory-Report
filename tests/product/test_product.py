from inventory_report.inventory.product import Product
import datetime


def test_cria_produto():
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

    assert product.id == product_data["id"]
    assert product.nome_do_produto == product_data["nome_do_produto"]
    assert product.nome_da_empresa == product_data["nome_da_empresa"]
    assert product.data_de_fabricacao == str(
        product_data["data_de_fabricacao"]
    )
    assert product.data_de_validade == str(product_data["data_de_validade"])
    assert product.numero_de_serie == product_data["numero_de_serie"]
    assert (
        product.instrucoes_de_armazenamento
        == product_data["instrucoes_de_armazenamento"]
    )
