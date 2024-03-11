from util import average


Total_values = int(input("Enter the number of values "))
list_of_Input =[]
for i in range(Total_values):
    Input = int(input(f"Enter the value: "))
    list_of_Input.append(Input)

average(list_of_Input)
