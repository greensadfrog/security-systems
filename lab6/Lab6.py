from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512
from Crypto.Cipher import AES


def rsa_sign(plaintext, key, hash_algorithm=Crypto.Hash.SHA512):
    signer = PKCS1_v1_5.new(RSA.importKey(key))
    hash_value = hash_algorithm.new(plaintext)
    return signer.sign(hash_value)


def rsa_verify(sign, plaintext, key, hash_algorithm=Crypto.Hash.SHA512):
    hash_value = hash_algorithm.new(plaintext)
    verifier = PKCS1_v1_5.new(RSA.importKey(key))
    return verifier.verify(hash_value, sign)


def kyys_rsa():
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    with open("private.pem", "w") as prv_file:
        print("{}".format(private_key.exportKey()), file=prv_file)

    with open("public.pem", "w") as pub_file:
        print("{}".format(public_key.exportKey()), file=pub_file)
    return private_key, public_key


def main():
    while True:
        print('Выберите режим - \n'
              '1)подпись + шифрование - "1"\n'
              '2)шифрование - "2"')
        try:
            a = int(input())
            if a == 1:
                private_key, public_key = kyys_rsa()
                message = "The answer is no"
                signature = rsa_sign(message.encode(encoding='utf-8'), private_key.exportKey(format='PEM'))
                obj = AES.new('KEYKEYKEYKEYKEYK', AES.MODE_CBC, 'This is an IV456')
                ciphertext = obj.encrypt(message)
                obj2 = AES.new('KEYKEYKEYKEYKEYK', AES.MODE_CBC, 'This is an IV456')
                import base64
                import sys
                result = rsa_verify(signature, message.encode('utf-8'), public_key.exportKey(format='PEM'))
                print(result)
                print(str(obj2.decrypt(ciphertext)))
            elif a == 2:
                message = "The answer is no"
                obj = AES.new('KEYKEYKEYKEYKEYK', AES.MODE_CBC, 'This is an IV456')
                ciphertext = obj.encrypt(message)
                obj2 = AES.new('KEYKEYKEYKEYKEYK', AES.MODE_CBC, 'This is an IV456')
                import base64
                import sys
                print(str(obj2.decrypt(ciphertext)))
        except:
            print('pass')


if __name__ == '__main__':
    main()
