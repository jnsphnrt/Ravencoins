from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256


def generate_sk():
    key = RSA.generate(3072)
    with open('secret_key.pem', 'wb') as f_out:
        f_out.write(key.export_key(format='PEM'))
    return key


def generate_pk(secret_key):
    pk = secret_key.public_key()
    with open('public_key.pem', 'wb') as f_out:
        f_out.write(pk.export_key(format='PEM'))
    return pk


def import_key(file_name):
    with open(file_name, 'rb') as f_im:
        key = RSA.import_key(f_im.read())
    return key


def encrypt(pk_receiver, msg):
    cipher = PKCS1_OAEP.new(pk_receiver)
    c = cipher.encrypt(msg)
    return c


def decrypt(sk, c):
    cipher = PKCS1_OAEP.new(sk)
    msg = cipher.decrypt(c)
    return msg


def footprint(pk):
    hasher = SHA256.new(pk)
    return hasher.digest()
