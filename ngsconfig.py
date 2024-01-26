# -*- coding: utf-8 -*-

"""
    Arquivo que le o arquivo f'{PROJECT_NAME}.ini'
"""

from configparser import ConfigParser
from crypto import decrypt_password

PROJECT_NAME = 'NgsPadrao'

CONFIG = ConfigParser()
CONFIG.read(f'{PROJECT_NAME}.ini')

NGS_CONFIG = CONFIG['config']
EMP, DIR_LOG = NGS_CONFIG['emp'], NGS_CONFIG['diretorio_log']

DB = CONFIG['database']
ORACLE_USER, PASS_DB, CLIENT = DB['user'], DB['password'], DB['client_dir']
HOST, PORT, SERVICE = DB['host'], int(DB['port']), DB['service']

ORACLE_PASS = decrypt_password(encrypted_password=PASS_DB.encode())

if __name__ == '__main__':
    print(ORACLE_PASS)
