import unittest
from book import Book


class TestBook(unittest.TestCase):
    """Tests the Book class"""

    def test_book_instance(self):
        the_beach = Book('The Beach', 'Alex Garland', 'Novel', 102)
        self.assertIsInstance(the_beach, Book, msg = 'The object should be an instance of the Book class')
        
    def test_object_type(self):
        the_beach = Book('The Beach', 'Alex Garland', 'Novel', 102)
        self.assertTrue((type(the_beach) is Book), msg = 'The object should be a type of Book')
        
    
if __name__ == '__main__':
    unittest.main(exit=False)