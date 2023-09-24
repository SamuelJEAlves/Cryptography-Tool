from cryptography.fernet import Fernet

secretKey = Fernet.generate_key()

fernet = Fernet(secretKey)

def EncryptPassword(password):
    return fernet.encrypt(password.encode()).decode()

def DecryptPassword(encryptedPassword):
    return fernet.decrypt(encryptedPassword.encode()).decode()

mainPassword = input('Enter password:')
encryptedPassword = EncryptPassword(mainPassword)
decryptedPassword = DecryptPassword(encryptedPassword)

print(f'Senha Desprotegida: {mainPassword}')
print(f'Senha Criptografada: {encryptedPassword}')
print(f'Senha Descriptografada: {decryptedPassword}')