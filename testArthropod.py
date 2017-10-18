import unittest
from arthropod import Arthropod


class TestArthropod(unittest.TestCase):
    """Tests the Arthropod class"""

    def test_arthropod_instance(self):
        the_beach = Arthropod('The Beach', 'Alex Garland', 'Novel', 102)
        self.assertIsInstance(the_beach, Book, msg = 'The object should be an instance of the Book class')
        
    def test_object_type(self):
        the_beach = Arthropod('The Beach', 'Alex Garland', 'Novel', 102)
        self.assertTrue((type(the_beach) is Book), msg = 'The object should be a type of Book')
        
    
if __name__ == '__main__':
    unittest.main(exit=False)