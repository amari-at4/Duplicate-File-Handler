# write your code here
for number in range(1, 11):
    with open(f"file{number}.txt", "w") as file:
        file.write(f"{number}\n")
