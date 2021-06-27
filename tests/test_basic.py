
from run import app
import unittest

class BasicTests(unittest.TestCase):

    def test_book(self):
        tester = app.test_client(self)
        response = tester.get('/book/2', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        data = b'[{"id": "7", "title": "Introduction to African Oral Literature and Performance", "author": "Bayo Ogunjimi", "authors": "Bayo Ogunjimi, Abdul Rasheed Na\'allah", "isbn13": "9.78159E+12", "isbn10": "1592211518", "price": "$23.95", "publisher": "Africa World Press", "pubyear": "2006", "subjects": "Africa - Anthropology & Sociology, African Folklore & Mythology, Oral Tradition & Storytelling, General & Miscellaneous African Literature - Literary Criticism, African Literature Anthologies, Fables, Fairy Tales, & Folk Tales - Literary Criticism", "lexile": "", "pages": "146", "dimensions": "8.30 (w) x 5.30 (h) x 0.80 (d)"}]'
        self.assertTrue((response.data, data))

    def test_filter_book(self):
        tester = app.test_client(self)
        response = tester.get('/book_filter/Jesse Grant', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        data = b'[{"id": "7", "title": "Introduction to African Oral Literature and Performance", "author": "Bayo Ogunjimi", "authors": "Bayo Ogunjimi, Abdul Rasheed Na\'allah", "isbn13": "9.78159E+12", "isbn10": "1592211518", "price": "$23.95", "publisher": "Africa World Press", "pubyear": "2006", "subjects": "Africa - Anthropology & Sociology, African Folklore & Mythology, Oral Tradition & Storytelling, General & Miscellaneous African Literature - Literary Criticism, African Literature Anthologies, Fables, Fairy Tales, & Folk Tales - Literary Criticism", "lexile": "", "pages": "146", "dimensions": "8.30 (w) x 5.30 (h) x 0.80 (d)"}]'
        self.assertTrue((response.data, data))


if __name__ == '__main__':
    unittest.main()