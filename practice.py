def sumOfNumbers (x, y):
    return x + y

x = int(input("Enter a number "))
y = int(input("Enter another number "))
sum = sumOfNumbers(x, y)
print(sum)

#Return the next number from an integer passed
def nextNumber (num):
    return num + 1
num = int(input("Enter an integer "))
print(nextNumber(num))

#Convert minutes into seconds
def convertMinToSec (minutes):
    return minutes * 60
minutes = int(input("Enter a time in minutes "))
print(f'{convertMinToSec(minutes)} seconds')

#Area of Triangle
def areaOfTriangle(base, height):
    return 1/2 * (base * height)

base = int(input("Enter the base of a triangle "))
height = int(input("Enter the height of a triangle "))
print(areaOfTriangle(base, height))

#Convert hours to seconds
def hoursToSeconds(hours):
    return hours * 3600
hours = int(input("Enter a time in hours "))
print(f'{hours}hours to seconds is {hoursToSeconds(hours)} seconds')

#Perimeter of a rectangle
def perimeterOfRectangle (length, width):
    return 2 * (length + width)
length = int(input("Enter the length of a rectangle "))
width = int(input("Enter the width of a rectangle "))
print(f'Perimeter of the rectangle is {perimeterOfRectangle(length, width)}')