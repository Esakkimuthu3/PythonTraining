try:
    number = int(input("Enter a number:"))
    print(1 / number)
except ZeroDivisionError:
    print("You cant divide by zero Idiot")
except ValueError:
    print("Enter only numbers please!")
finally:
    print("Do some cleanup here")            