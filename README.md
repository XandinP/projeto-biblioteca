# projeto-biblioteca
projeto para gestao de biblioteca


# Como rodar o projeto

## Instalar dependencias

`pip install rich`
`pip install tabulate`
`pip install cx_Oracle`


## Atualizar as credenciais do banco
- Va para ./src/db/database_manager.py
- Atualize os campos `user`, `password` e outros se necessario

## Rodar script the inicialiacao
`python ./src/init_data.py`

## Iniciar aplicacao
`python ./src/main.py`