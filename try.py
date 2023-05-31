import prime

p = prime.Prime(1000000)
p.cal()
print(p.isPrime(5))
print(p.isPrime(100))
print(p.listPrime(0, 1000))
print(p.countPrime(0, 1000000))
