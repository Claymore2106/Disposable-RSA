from os import urandom
from base64 import b16encode

def generateNum(size):
    sHex = ""
    k = 0                           # Byte counter
    while k < size:
        rand = urandom(1)           # Random byte
        rand = b16encode(rand)      # Set to hex
        rand = str(rand)            # String
        rand = rand[2:-1]           # Remove '0x'
        sHex += rand                # Build number
        k += 1
    sHex = int(sHex, 16)
    print('Random Seed:', sHex)
    print("Bit length:", sHex.bit_length())
    return sHex

def testPrime(randNum):
    k = 1
    s = str(randNum)
    l = len(s)
    t = int(s[l-1:])
    
    # Ensure Odd
    
    print('[%i] Last num: %i' % (k, t))
    if (t % 2) == 0:
        print('[%i] Making odd: %i --> %i' % (k, t, (t+1)))
        randNum = randNum + 1
        print('[%i] %i' % (k, randNum))
    
    # Test for Prime
    
    

def main():
    randNum = generateNum(16)        # Bytes of entropy
    testPrime(randNum)

if __name__ == "__main__":
    main()