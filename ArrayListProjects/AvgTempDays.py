def average(temp_list):
    avg = sum(temp_list)/len(temp_list)
    return avg
    
days = int(input("How many days temp?: "))
temp = []
for i in range(1, days + 1):
    temp.append(float(input(f"Day {i}'s temp: ")))

average_of_days = average(temp)
print(f"Average = {average_of_days}")

counter = 0
for i in range(0, days):
    if temp[i] > average_of_days:
        counter += 1

print(f"{counter} day(s) above average")