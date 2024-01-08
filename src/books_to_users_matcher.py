import json
from csv import DictReader

from files import BOOKS_FILE, USERS_FILE


def read_books(file_name):
    result_list = []

    with open(file_name, newline='') as books_file:
        reader = DictReader(books_file)
        for row in reader:
            result_list.append(dict(row))

    return result_list


def read_users(file_name):
    with open(file_name) as users_file:
        users = json.loads(users_file.read())

    return users


def modify_books(books):
    new_books = []
    for i in range(len(books)):
        new_dict = {'title': books[i]['Title'], 'author': books[i]['Author'],
                    'pages': books[i]['Pages'], 'genre': books[i]['Genre']}
        new_books.append(new_dict)

    return new_books


def modify_users(users):
    new_users = []
    for i in range(len(users)):
        new_dict = {'name': users[i]['name'], 'gender': users[i]['gender'],
                    'address': users[i]['address'], 'age': users[i]['age']}
        new_users.append(new_dict)

    return new_users


def user_books_assignment(books, users):
    number_books = len(books)
    number_users = len(users)

    coefficient = number_books // number_users
    remainder = number_books % number_users

    for i, user in enumerate(users):
        list_of_books_for_user = []
        for j in range(i * coefficient, (i + 1) * coefficient):
            list_of_books_for_user.append(books[j])
        if i < remainder:
            list_of_books_for_user.append(books[len(users) * coefficient + i])

        user['books'] = list_of_books_for_user
    return users


def save_result(users):
    with open("results.json", "w") as f:
        data = json.dumps(users, indent=4)
        f.write(data)


if __name__ == '__main__':
    books_ = modify_books(read_books(BOOKS_FILE))
    users_ = modify_users(read_users(USERS_FILE))
    save_result(user_books_assignment(books_, users_))
