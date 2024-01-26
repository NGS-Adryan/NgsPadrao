# -*- coding: utf-8 -*-

"""
    Arquivo contendo função para descriptografar a senha do banco
"""

from cryptography.fernet import Fernet

def decrypt_password(encrypted_password: bytes) -> str:
    """Função para descriptografar a senha do banco

    Args:
        encrypted_password (bytes): Passando a senha encriptografada

    Returns:
        str: Senha do banco
    """
    KEY = open('token.key', 'rb').read()
    return Fernet(KEY).decrypt(encrypted_password).decode()
    

if __name__ == '__main__':
    print()
