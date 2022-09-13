#1 howManyEven() is counting the number of even numbers between 0 and the number, howManyEven(9) = 5
#2 isOdd(3) returns true because the remainder when 3/2 doesn't = 0
#3 see code below
#4 n = 3 // 4
#input: a number
#output: the number of even numbers between that number and 0 (including 0 and the number)
def howManyEven(num):
    count = 0
    if num < 0:
        num *= -1
    while(num >= 0):
        if isEven(num):
            count += 1
        num -= 1
    return count
    
#input: a number
#output: true/false depending on whether the number is even or not
def isEven(num):
    return num % 2 == 0
    
#input: a number
#output: true/false depending on whether the number is odd or not
def isOdd(num):
    return num % 2 != 0
  
def noChange(cents):
  if cents % 100 == 0:
    print(cents // 100)
    return "Hoorah!"
  elif cents % 200 != 0
    print(cents // 100)
  return "Keep the change!"


#input: num–an int of some kind
#output: the positive factorial of num
def oldFactorial(num):
    total = 1
    if num < 0:
        num *= -1
    while(num == num):
        if num <= 0:
            break
        else:
            total = total * num
            num -= 1
    return total
  
    
def main():
    print(howManyEven(4))
    print(howManyEven(9))
    print(isOdd(12))
    print(isEven(12))
    print("TESTING", noChange(100))
    print("TESTING", noChange(225)
