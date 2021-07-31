from cryptography.fernet import Fernet

def encrypt(filepath, key):
    f = Fernet(key)

    with open(filepath, 'rb') as file:
        file_data = file.read()
        enc_data = f.encrypt(file_data)
        with open(filepath, 'wb') as file:
            file.write(enc_data)

def decrypt(filepath, key):
    f = Fernet(key)
    with open(filepath, 'rb') as file:
        file_data = file.read()

        dec_data = f.decrypt(file_data)
        with open(filepath, 'wb') as file:
            file.write(dec_data)

#encrypt('description.txt', 'MAmXiFE9eZddhC3MhW4DSopE5yalDtPR1b57_ycCtMQ=')
#decrypt('description.txt', 'MAmXiFE9eZddhC3MhW4DSopE5yalDtPR1b57_ycCtMQ=')