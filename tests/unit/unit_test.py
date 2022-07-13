import unittest
from project.persistence.users_dao import get_users

class userdb(unittest.TestCase):
    
    def test_get_users(self):
        result=get_users()
        print(result)
        self.assertTrue(len(result)>0)
