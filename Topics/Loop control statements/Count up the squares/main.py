# put your python code here
value = []
while True:
    number = int(input())
    value.append(number)
    if sum(value) == 0:
        print(sum([entered_number ** 2 for entered_number in value]))
        break
