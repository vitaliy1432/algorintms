n = int(input('Введите количество карточек: '))
k = int(input('Введите коэффициент, отвечающий за максимальную разницу в баллах: '))
x = list(map(int, input('Введите через пробел карточки: ').split()))

cards = dict()
for i in x:
    if i not in cards:
        cards[i] = 1
    else:
        cards[i] += 1

cards_without_repeat = list(cards.keys())
cards_without_repeat.sort()
result = 0
r = 0
duplicated_cards = 0

for l in range(len(cards_without_repeat)):
    while (r < len(cards_without_repeat)) and (cards_without_repeat[l]*k >= cards_without_repeat[r]):
        if cards[cards_without_repeat[r]] >= 2:
            duplicated_cards += 1
        r += 1
    range_length = r - l
    if cards[cards_without_repeat[l]] >= 2:
        result += (range_length - 1)*3
        duplicated_cards -= 1
    if cards[cards_without_repeat[l]] >= 3:
        result += 1
    result += (range_length - 1)*(range_length - 2)*3 + duplicated_cards*3

print(f'Он может составить {result} вариантов счёта')

