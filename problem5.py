n = int(input("enter the number of days: "))
measures = []
for i in range(n):
    m = int(input("enter the measurement for next day: "))
    measures.append(m)

for i in range(n):
    print(f"Day {i + 1}: {measures[i]} cm")

print(f"First height: {measures[0]}")
print(f"Last height: {measures[-1]}")
print(f"Change: {measures[-1] - measures[0]}")