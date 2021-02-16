import unittest
from unittest import TestCase

import sqlite3

import config

test_db_path = 'test_art.sqlite'
config.db_path = test_db_path

import db

from model import Artist

class TestDB(TestCase):

    def setUp(self):
        # ensure tables exist and clear DB so it's empty before tests start

        db.create_table() 

        with sqlite3.connect('test_art.sqlite') as conn:
            conn.execute('DELETE FROM artist')
        conn.close()
        

    def test_add_artist(self):
        example = Artist('Example', 25)
        added = db.add_artist(example)

        self.assertTrue(added)

        expected_rows = [ ('Example', 25) ]
        actual_rows = self.get_all_data()
    
        # assertCountEqual will compare two iterables, e.g. a list of tuples returned from DB
        self.assertCountEqual(expected_rows, actual_rows)

        example2 = Artist('Another Example', 30)
        added2 = db.add_artist(example2)

        self.assertTrue(added2)

        expected_rows = [ ('Example', 25), ('Another Example', 30) ]
        actual_rows = self.get_all_data()

        self.assertCountEqual(expected_rows, actual_rows)


    def test_add_duplicate_name_artist(self):

        example = Artist('Example', 25)
        added = db.add_artist(example)
        
        example2 = Artist('Example', 40)   # same name
        added2 = db.add_artist(example2)

        self.assertFalse(added2)

        expected_rows = [ ('Example', 25) ]  # only one artist 
        actual_rows = self.get_all_data()

         # assertCountEqual will compare two iterables, e.g. a list of tuples returned from DB
        self.assertCountEqual(expected_rows, actual_rows)




    def get_all_data(self):
        with sqlite3.connect('test_art.sqlite') as conn:
            rows = conn.execute('SELECT * FROM artist').fetchall()
        conn.close()
        return rows


if __name__ == '__main__':
    unittest.main()