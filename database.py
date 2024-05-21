"""Arquivo encarregado de lidar com o banco de dados, fazendo a conexão
e executando as querys do arquivo `dbquerys.py`."""

from oracledb import init_oracle_client, makedsn, connect

from ngsconfig import CLIENT, HOST, PORT, SERVICE, ORACLE_USER, ORACLE_PASS
from dbquerys import QUERY_TEST

init_oracle_client(lib_dir=CLIENT)
DSN = makedsn(host=HOST, port=PORT, service_name=SERVICE)

def test_connection() -> bool:
    """Função para testar se está funcionando a conexão com o banco.

    :return: bool - Se está ou não funcionando.
    """
    with connect(DSN, user=ORACLE_USER, password=ORACLE_PASS) as CONNECTION:
        with CONNECTION.cursor() as CURSOR:
            CURSOR.execute(QUERY_TEST)
            return True if CURSOR.fetchall() else False


if __name__ == "__main__":
    print(test_connection())
