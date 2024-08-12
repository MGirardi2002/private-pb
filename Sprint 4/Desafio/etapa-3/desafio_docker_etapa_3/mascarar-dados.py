import hashlib

entrada = input("Digite uma string para mascarar: ")

hash_object = hashlib.sha1(entrada.encode())
hex_dig = hash_object.hexdigest()

print("Hash SHA-1:", hex_dig)
