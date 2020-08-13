
class Crypto:

    def getRandomNumber(x, y):
        return random.randint(x, y)

    def isPrime(n):
        if n < 3:
            return n == 2
        if 0 == n % 2:
            return False
        for i in range(3, n // 2):
            if 0 == n % i:
                return False
        return True

if __name__ == "__main__":

    for i in range(0, 110):
        if Crypto.isPrime(i):
            print(i)