number_of_lines = int(input())

winners = []
for _ in range(number_of_lines):
    (player_name, wins) = input().split()
    if wins == "win":
        winners.append(player_name)

print(winners)
print(len(winners))
