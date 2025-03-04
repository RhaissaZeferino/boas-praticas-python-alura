import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Bem-vindo à API de Recomendação de Produtos"
    }


def test_criar_usuario():
    response = client.post("/usuarios/", params={"nome": "Fulano"})
    assert response.status_code == 200
    usuario = response.json()
    assert usuario["nome"] == "Fulano"
    assert usuario["id"] == 1


def test_listar_usuarios():
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "nome": "Fulano"}]


def test_criar_produto():
    response = client.post(
        "/produtos/",
        json={
            "nome": "Produto 1",
            "categoria": "Categoria 1",
            "tags": ["tag1", "tag2"],
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Produto 1"


def test_listar_produtos():
    response = client.get("/produtos/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_adicionar_historico_compras():
    response = client.post(
        "/historico_compras/1",
        json={"produtos_ids": [1]},
    )
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Histórico de compras atualizado"}


def test_recomendar_produtos():
    response = client.post(
        "/recomendacoes/1",
        json={"categorias": ["Categoria 1"], "tags": ["tag1"]},
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
