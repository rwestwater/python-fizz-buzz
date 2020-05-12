def fizzbuzz(number):
    result = ""
    
    if number % 3 == 0:
        result += "Fizz"

    if number % 5 == 0:
        result += "Buzz"

    if number % 7 == 0:
        result += "Boop"

    if result == "":
        result = str(number)

    return result