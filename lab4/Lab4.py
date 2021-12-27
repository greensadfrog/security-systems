import math


# ================ First part==================
def fdp(msg, key, p):
    """this function performs fast discrete potentiation"""
    binaryKey = bin(key).replace('0b', '')
    cipherE = 1
    for i in range(len(binaryKey)):
        cipherE = ((cipherE ** 2) * (msg ** int(binaryKey[i]))) % p
    return cipherE


msg = int(input('Input the message: '))
key = int(input('Input the public key: '))
p = int(input('Input P-parameter: '))

print('\nCipher E = ', fdp(msg, key, p), '\n')


# ================ Second part==================
def generatePrimeNumber(p_max, simpleSmallNumber):
    """this function generates large prime numbers"""
    k = math.ceil(math.log(p_max / 2, simpleSmallNumber))
    p1 = 2 * (simpleSmallNumber ** k) + 1
    p2 = 2 * (simpleSmallNumber ** k) - 1
    if fdp(2, p1 - 1, p1) == 1:
        p = p1
    if fdp(2, p2 - 1, p2) == 1:
        p = p2
    else:
        while fdp(2, p1 - 1, p1) != 1:
            p1 += 2
        p = p1
    return p


def IsPrime(n):
    """this function checks numbers for simplicity"""
    d = 2
    while n % d != 0:
        d += 1
    return d


p_max = int(input('Input Pmax number: '))
simpleSmallNumber = int(input('Input small simple number: '))

if IsPrime(simpleSmallNumber) == simpleSmallNumber:
    print('\nPrime number P was generated: ', generatePrimeNumber(p_max, simpleSmallNumber))
else:
    print("\nThe small number entered is not prime. Try another one.")
