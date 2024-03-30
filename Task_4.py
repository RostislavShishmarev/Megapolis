import csv


def create_books_list():
    """
    Function to get list of dicts with information about books
    Dict format:
    {
      'author': list of authors
      'title': book title
      'date': publication date
      'rating': float number of rating
      'isbn': book ISBN
    }
    :return: list of dicts
    """
    with open('books.txt', encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter='%'))[1:]  # Cut headers
    # Rows format: 0 - id, 1 - isbn, 2 - authors, 3 - year, 4 - title, 5 - rating

    result = []
    for row in data:
        result.append({
            'authors': row[2].split(', '),
            'title': row[4],
            'date': row[3],
            'rating': float(row[5].replace(',', '.')),
            'isbn': row[1],
        })
    return result


def get_books_number_dict_by_author():
    """
    Function to get num,ber of books written by each author
    :return: dict with keys - authors and values - numbers of their books
    """
    result = {}
    for book in create_books_list():
        for author in book['authors']:
            result[author] = result.get(author, 0) + 1
    return result


def write_top_n_authors(n):
    """
    Writes to file 'top_<n>_authors.csv' top n authors by number of their books
    :param n: number best authors to write
    :return: None
    """
    top_dict = get_books_number_dict_by_author()
    authors = list(top_dict.keys())
    authors.sort(key=lambda author: -top_dict[author])
    with open(f'top_{n}_authors.csv', mode='w', encoding='utf-8') as file:
        file.write('\n'.join(authors[:n]))


if __name__ == '__main__':
    write_top_n_authors(10)
