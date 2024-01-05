import os.path

WORK_FOLDER = os.path.dirname(os.path.abspath(__file__))


def get_path(filename):
    return os.path.join(WORK_FOLDER, filename)


BOOKS_FILE = get_path("books.csv")
USERS_FILE = get_path("users.json")
