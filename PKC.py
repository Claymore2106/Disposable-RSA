import random
import binascii


# x=b'test'
# x=binascii.hexlify(x)
# x
# b'74657374'
# y=str(x,'ascii')
# y
# '74657374'
# x=binascii.unhexlify(x)
# x
# b'test'
# y=str(x,'ascii')
# y
# 'test'

# https://stackoverflow.com/questions/14010551/how-to-convert-between-bytes-and-strings-in-python-3


def getInput():
    p = int(input("Enter prime number 'a': "))
    q = int(input("Enter prime number 'b': "))
    
    print()
    print("P = %i" % p)
    print("Q = %i" % q)
    return p, q


def GCD(a, b):
    while b: #b != 0
        a,b = b, a%b
    return a == 1


def genCoprime(totient):
    # e is coprime phi(n) if 1<e<phi(n) and GCD(e,phi(n))
    coprime = False
    k = 0
    while coprime == False:
        e = random.randint(2, (totient - 1))
        k += 1
        if k == 100:
            break
            
        if GCD(e, totient) == 1:
            print("[%i] Coprime found: %i" % (k,e))
            coprime = True
            return e
        else:
            print("[%i] Tried %i... Failed" % (k, e))

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm


def xGCD(b, n): #  ax + by = g = gcd(a, b).
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0


# x = mulinv(b) mod n, (x * b) % n == 1
def mulInv(b, n):
    g, x, _ = xGCD(b, n)
    if g == 1:
        return x % n


def rsaEncrypt(m, e, n):
    print('-----------')
    encryptedM = ""
    for s in m:
        b = s.encode('UTF-8')
        h = binascii.hexlify(b)
        print('[%s] h: %s' % (s, h))
        i = int(h, 16)
        print('[%s] i: %s' % (s, i))
        #encrypted
        eI = (i**e) % n
        print('[%s] eI: %s' %(s, eI))
        eH = hex(eI)
        print('[%s] eH: %s' % (s, eH))
        print('-----------')
        #eS = str(eH)[2:]
        #print('eS:', eS)
        #if (len(eS) % 2) != 0:
            #eS = eS.zfill(len(eS)+1)
        
        encryptedM += eH
    return encryptedM


def parseHex(m):
    hB = []
    pos = 2
    L = 1
    sec = m[pos:pos+L]
    while len(m) >= (pos + L):
        while 'x' not in sec and len(m) >= (pos + L):
            sec = m[pos:pos+L]
            print('[%i:%i] %s' % (pos, pos+L, sec))
            L += 1

        if (pos+L) <= len(m):
            sec = sec[:-2]
            print(sec)
            hB.append(sec)
            pos = (pos + L) - 1
            L = 1
        else:
            print(sec)
            hB.append(sec)
            
    print('\n' + str(hB) + '\n')
    return hB


def rsaDecrypt(m, d, n):
    hB = parseHex(m)
    decryptedM = "" 
    
    for h in hB:
        print('[0x%s] --------' % h)
        eI = int(h, 16)
        print('eI:', eI)
        i = (eI**d) % n
        print('i:', i)
        h2 = (hex(i))[2:]
        b = binascii.unhexlify(h2)
        c = str(b, 'UTF-8')
        print('c:', c)
        decryptedM += c
    
    return decryptedM


def main():
    p, q = 61, 53 # getInput()
    print ("P = %i; Q = %i" % (p, q))
    n = (p * q)
    print("N = %i" % n)
    totient = ((p - 1) * (q - 1))
    print("T = %i" % totient)
    e = genCoprime(totient)
    print("E = %i (public)" % e)
    d = mulInv(e, totient)
    print("D = %i (private)" % d)
    m = 'ABC'
    #m = bytes(m, 'UTF-8')
    print("\nMessege: %s\n" % m)
    encryptedM = rsaEncrypt(m, e, n)
    print("\nEncrypted M:", encryptedM)
    print("Length:", len(encryptedM))
    decryptedM = rsaDecrypt(encryptedM, d, n)
    print("Decrypted M:", decryptedM)


if __name__ == "__main__":
    main()
