# projeto-biblioteca
projeto para gestao de biblioteca escolar


# Como rodar o projeto

## Instalar dependencias

`pip install rich`
`pip install tabulate`
`pip install cx_Oracle`

- Para rodar em linux e necessario ter o InstantClient
- Siga as intruções nesse [link](https://csiandal.medium.com/install-oracle-instant-client-on-ubuntu-4ffc8fdfda08)

## Atualizar as credenciais do banco
- Va para ./src/db/database_manager.py
- Atualize os campos `user`, `password` e outros se necessario

## Rodar script the inicialiacao
- Navegue ate a pasta src 
`cd src`
`python init_data.py`

## Iniciar aplicacao
- Navegue ate a pasta src 
`cd src`
`python .main.py`