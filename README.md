# flask-numeros

A API deste repositório transforma numeros em palavras.
para acessar a API basta fazer requisições no endereço: `127.0.0.1:3000/<numero>` substituindo <numero> pelo numero desejado.
Para utilizar localmente no seu PC execute os seguintes comandos

``` bash
pip install -r requirements.txr
python app.py
```

# Rodando os testes

`pytest test_core.py`

# Rodando com Docker

Para rodar 
`docker-compose up`

# Exemplo de uso

``` bash
$ curl http://localhost:3000/94587
{ "extenso": "noventa e quatro mil e quinhentos e oitenta e sete" }
```
