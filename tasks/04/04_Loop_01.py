receive_input = True

list_of_numbers = []
numbers_of_input = 0

while (receive_input):
  user_input = input()
  if (user_input == "q"):
    receive_input = False
    if (numbers_of_input == 0): print("No Data")
    break
  
  numbers_of_input += 1
  list_of_numbers.append(float(user_input))

  

if numbers_of_input:
  average = sum(list_of_numbers) / numbers_of_input
  average = round(average, 2)
  print(average)
