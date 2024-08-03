numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Необходимо составить список простых и список непростых элементов из nambers
primes = []       # простые
not_primes = []   # не простые

for i in numbers:               # перебираем элементы
   if i == 1: continue          # кроме равных 1
   is_prime = True
   for j in range(2, i):        # перебираем делители, кроме равных 1
       if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
   if is_prime == True:
       primes.append(i)
print(primes)
print(not_primes)

