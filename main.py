from math_game import add
from math_game import substract
from math_game import multiply
from math_game import divide

def game():
  score = 0
  while True:
    print('======== Menu ========\n1. Add\n2. Substract \n3. Multiply\n4. Divide')
    operation = int(input("Choose an operation:"))
    num_1 = input('Enter first number: ')
    num_2 = input('Enter second number: ')
    answer = int(input('Enter you answer: '))
    if operation == 1:
      result = add(num_1, num_2)
      if result == answer:
        score += 1
        print('Correct!!')
      else:
        print('Incorrect')
        break
    if operation == 2:
      result = substract(num_1, num_2)
      if result == answer:
        score += 1
        print('Correct!!')
      else:
        print('Incorrect')
        break
    if operation == 3:
      result = multiply(num_1, num_2)
      if result == answer:
        score += 1
        print('Correct!!')
      else:
        print('Incorrect')
        break
    if operation == 4:
      result = divide(num_1, num_2)
      if result == answer:
        score += 1
        print('Correct!!')
      else:
        print('Incorrect')
        break
    print(f"======== Game Over ========\nYour score is {score}\nKeep going!")
    
game()
