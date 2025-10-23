## Write a Python program that invoke square root function after specific milliseconds.

import time
import math

num = int(input("Enter a number: "))
milliseconds = int(input("Enter delay in milliseconds: "))

#переводим миллисекунды в секунд
time.sleep(milliseconds / 1000)

#выводим квадратный корень
print("Square root is:", math.sqrt(num))


