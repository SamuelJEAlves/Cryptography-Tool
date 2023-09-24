from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()

fernet = Fernet(secret_key)

def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()

main_password = input('Enter password:')
encrypted_password = encrypt_password(main_password)
decrypted_password = decrypt_password(encrypted_password)

print(f'Senha Desprotegida: {main_password}')
print(f'Senha Criptografada: {encrypted_password}')
print(f'Senha Descriptografada: {decrypted_password}')