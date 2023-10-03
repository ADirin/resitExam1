n = 100
output = "X"
if n >= 10:
    print(output)
    if n > 150:
        output = "Y"
    else:
        output = "Z"
else:
    print("E")
print(output)
print('---------------------------')

i = 1
while i % 5 != 0:
    print(i)
    i = i + 2
print(i)

print('---------------------------')
for num in range(6, 1, -2):
    print(f"{num}. item")

print('---------------------------')

people = ("Maria", "Ahmed", "Donald", "Olga")
p1, p2, p3, p4 = people
print(p2)
print(people[2])
if p1 not in people:
    print(people)

print('-------------')


def operate(values, limits):
    sum = 0
    min = limits[0]
    max = limits[1]
    for nr in values:
        if min <= nr <= max:
            sum += nr
    return sum
