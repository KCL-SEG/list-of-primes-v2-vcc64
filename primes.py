"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError

    lastPrimeNumber = 0
    
    for i in range(number_of_primes):
        currentNumber = lastPrimeNumber
        currentNumberIsPrime = False

        while (not currentNumberIsPrime):
            for j in range(currentNumber):
                if (currentNumber % j == 0):
                    currentNumber += 1
                    break
                if (j == currentNumber-1):
                    currentNumberIsPrime = True
                    
        lastPrimeNumber = currentNumber
        list[i] = currentNumber

    return list
