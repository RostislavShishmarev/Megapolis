import csv


def compare(list1, list2, key=lambda x: x):
    """
    Function to make new sorted list from two sorted
    :param list1: first list of elements
    :param list2: second list of elements
    :param key: sorting key (function)
    :return: new list
    """
    res = []
    i, j = 0, 0
    while True:
        if i >= len(list1):
            res += list2[j:]
            break
        if j >= len(list2):
            res += list1[i:]
            break
        if key(list1[i]) <= key(list2[j]):
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    return res


def s_sort(list_, key=lambda x: x, start=0, end=None):
    """
    Function to sort iterable
    :param list_: list of elements
    :param key: sort key (function)
    :param start: start index of sorting
    :param end: end index of sorting
    :return: new list
    """
    if end is None:
        end = len(list_) - 1
    if start + 1 == end:
        els = [list_[start], list_[end]]
        return [min(els, key=key), max(els, key=key)]
    if end <= start:
        return [list_[start]]

    middle = (start + end) // 2
    list1 = s_sort(list_, key=key, start=start, end=middle)
    list2 = s_sort(list_, key=key, start=middle + 1, end=end)
    return compare(list1, list2, key=key)


if __name__ == '__main__':
    with open('books.txt', encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter='%'))[1:]
    best_3 = s_sort(data, key=lambda row: -float(row[5].replace(',', '.')))[:3]
    for row in best_3:
        print(f'{row[4]} - {row[2]} - {row[5]}')
