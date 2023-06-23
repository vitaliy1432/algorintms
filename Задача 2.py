def get_number_of_smaller(subsequence, number):
    l_range = 0
    r_range = len(subsequence) - 1
    while l_range < r_range:
        m = (l_range + r_range) // 2
        if subsequence[m] >= number:
            r_range = m
        else:
            l_range = m + 1
    if subsequence[l_range] < number:
        return len(subsequence)
    return l_range

def get_number_of_bigger(subsequence, number):
    return len(subsequence) - get_number_of_smaller(subsequence, number + 1)

def get_median(subsequence_1, subsequence_2):
    l_range = min(subsequence_1[0], subsequence_2[0])
    r_range = max(subsequence_1[-1], subsequence_2[-1])
    while l_range < r_range:
        m = (l_range + r_range) // 2
        number_of_smaller = get_number_of_smaller(subsequence_1, m) + get_number_of_smaller(subsequence_2, m)
        number_of_bigger = get_number_of_bigger(subsequence_1, m) + get_number_of_bigger(subsequence_2, m)
        if (number_of_smaller <= len(subsequence_1) - 1) and (number_of_bigger <= len(subsequence_1)):
            return m
        if number_of_bigger > len(subsequence_1):
            l_range = m + 1
        elif number_of_smaller > len(subsequence_1) - 1:
            r_range = m - 1
    return l_range

n = int(input('Введите количество последовательностей: '))
l = int(input('Введите количество элементов для каждой последовательности: '))

all_subsequences = []
for i in range(n):
    subsequence = []
    print(f'Ввод {i+1} последовательности: ')
    for j in range(l):
        subsequence.append(int(input()))
    all_subsequences.append(subsequence)

for i in range(n-1):
    for j in range(i + 1, n):
        print(f'Левая медиана объединения {i+1} и {j+1} последовательностей -- {get_median(all_subsequences[i], all_subsequences[j])}')
