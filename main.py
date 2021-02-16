""" Example methods from first iteration of program """
from model import Artist
import db


def main():
    setup()
    add_new_artist()


def setup():
    # any tasks the program needs to complete before it can start 
    db.create_table()


def add_new_artist():
    name = input('Enter name: ')
    age = int(input('Enter age: '))

    artist = Artist(name, age)
    added = db.add_artist(artist)

    # todo distinguish between added, duplicate, unexpected error 
    if added:
        print('Added artist')
    else:
        print('Duplicate artist')


if __name__ == '__main__':
    main()