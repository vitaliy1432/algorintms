def get_minutes(s):
    return int(s[:2])*60 + int(s[3:])

n = int(input('Введите количество городов: '))
m = int(input('Введите количество рейсов: '))

bus_number = [0]*(n+1)
check_bus_overflow = [0]*(n+1)
events = list()
night = 0

for i in range(m):
    print(f'Рейс {i+1}')
    departure_city = int(input('Введите номер города отправления: '))
    departure_time = get_minutes(input('Введите время отправления: '))
    arrival_city = int(input('Введите номер города прибытия: '))
    arrival_time = get_minutes(input('Введите время прибытия: '))
    if arrival_time < departure_time:
        night += 1
    check_bus_overflow[departure_city] -= 1
    check_bus_overflow[arrival_city] += 1
    events.append((departure_time, 1, departure_city))
    events.append((arrival_time, -1, arrival_city))

overflow = False
for i in range(n+1):
    if check_bus_overflow[i] != 0:
        overflow = True
if overflow:
    print(-1)
else:
    events.sort()
    for i in events:
        if i[1] == -1:
            bus_number[i[2]] += 1
        elif bus_number[i[2]] > 0:
                bus_number[i[2]] -= 1

    print(sum(bus_number) + night)
