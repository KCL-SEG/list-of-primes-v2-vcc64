"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError

    lastPrimeNumber = 1
    
    for i in range(number_of_primes):
        currentNumber = lastPrimeNumber + 1
        currentNumberIsPrime = False

        while (not currentNumberIsPrime):
            for j in range(2,currentNumber+1):
                if (currentNumber % j == 0 and not j == currentNumber):
                    currentNumber += 1
                    break
                elif (j == currentNumber):
                    currentNumberIsPrime = True

        lastPrimeNumber = currentNumber
        list.append(currentNumber)

    return list
