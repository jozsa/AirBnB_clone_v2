#!/usr/bin/python3
""" Tests for DBStorage """
import os
import unittest
import MySQLdb
import models
from models import State
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """Test DBStorage"""
    def setUp(cls):
        """Connect to MySQL database for testing"""
        if 'HBNB_TYPE_STORAGE' in os.environ and \
                os.environ['HBNB_TYPE_STORAGE'] == 'db':
            cls.conn = MySQLdb.connect(host=os.environ['HBNB_MYSQL_HOST'],
                                       user=os.environ['HBNB_MYSQL_USER'],
                                       passwd=os.environ['HBNB_MYSQL_PWD'],
                                       db=os.environ['HBNB_MYSQL_DB'])
            cls.cur = cls.conn.cursor()
            cls.storage = DBStorage()
            cls.storage.reload()
        else:
            pass

    @unittest.skipIf('HBNB_TYPE_STORAGE' not in  os.environ or
                     os.environ['HBNB_TYPE_STORAGE'] != 'db',
                     "Doesn't work with FileStorage")
    def test_db_storage_type(self):
        """ Test whether storage is DBStorage instance """
        self.assertTrue(isinstance(self.storage, DBStorage))
