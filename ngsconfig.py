# -*- coding: utf-8 -*-

"""
    Arquivo encarregado de ler o arquivo `{PROJECT_NAME}.ini` e
configurar as constantes.

Constantes
----
Do `Projeto`:
* `PROJECT_NAME`: Nome do projeto: "NgsImpTransdata"
* `EMP`: Empresa, para inserir no banco. EX: 1.
----
Do `Banco de dados`:
* `ORACLE_USER`: Usuário para se conectar no banco.
* `ORACLE_PASS` Senha para se conectar no banco.
* `CLIENT`: Caminho do InstantClient do oracle.
* `HOST`: Host de conexão.
* `PORT`: Porta da conexão.
* `SERVICE`: SID da conexão.
-----
"""

from configparser import ConfigParser

from crypto import decrypt_password

PROJECT_NAME = "NgsPadrao"

CONFIG = ConfigParser()
CONFIG.read(f"{PROJECT_NAME}.ini")

NGS_CONFIG = CONFIG["config"]
EMP, DIR_LOG = NGS_CONFIG["emp"], NGS_CONFIG["diretorio_log"]

DB = CONFIG["database"]
ORACLE_USER, PASS_DB, CLIENT = DB["user"], DB["password"], DB["client_dir"]
HOST, PORT, SERVICE = DB["host"], int(DB["port"]), DB["service"]
ORACLE_PASS = decrypt_password(encrypted_password=PASS_DB.encode())

if __name__ == "__main__":
    print(ORACLE_PASS)
