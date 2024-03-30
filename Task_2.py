import csv


def s_sort(list_, key=lambda x: x):
    return sorted(list_, key=key)


if __name__ == '__main__':
    with open('books.csv', encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter='%'))[1:]

    best_3 = s_sort(data, key=lambda row: -float(row[5].replace(',', '.')))[:3]
    for row in best_3:
        print(f'{row[4]} - {row[2]} - {row[5]}')
