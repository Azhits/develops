import unittest

class Library():
    
    def __init__(self, library_name, adress, city):
        self.library_name = library_name
        self.adress = adress
        self.city = city

    def rename(self, new_library_name):
        self.library_name = new_library_name
    
class Fund_Library():
    
    def __init__(self, fund_name, library, number_books, number_magazines, number_newspapers,
                 number_collections, number_dissertations, number_reports):
        self.fund_name = fund_name
        self.library = library
        self.number_books = number_books
        self.number_magazines = number_magazines
        self.number_newspapers = number_newspapers
        self.number_collections = number_collections
        self.number_dissertations = number_dissertations
        self.number_reports = number_reports

    def change_number_books(self, new_number_books):
        self.number_books = new_number_books

class Literature_Type():
    
    def __init__(self, literature_type_name):
        self.literature_type_name = literature_type_name

    def rename_literature_type(self, new_literature_type_name):
        self.literature_type_name = new_literature_type_name

class Worker():
    
    def __init__(self, worker_surname, library, post, year_birth, year_admission, education, salary):
        self.worker_surname = worker_surname
        self.library = library
        self.post = post
        self.year_birth = year_birth
        self.year_admission = year_admission
        self.education = education
        self.salary = salary

    def change_salary(self, new_salary):
        self.salary = new_salary

class Fund_Replenishment():
    
    def __init__(self, fund, worker, date, literature_source_name, literature_type,
                         publishing, date_publication, number_copies):
        self.fund = fund
        self.worker = worker
        self.date = date
        self.literature_source_name = literature_source_name
        self.literature_type = literature_type
        self.publishing = publishing
        self.date_publication = date_publication
        self.number_copies = number_copies

    def increase_number_copies_on(self, amount):
        self.number_copies += amount


class Test_Library(unittest.TestCase):

    def setUp(self):
        self.library = Library("City Library №1", "Embankment of the Northen Dvina 135", "Arkhangelsk")

    def test_library_rename(self):
        test_name = "City Library №2"
        self.library.rename("City Library №2")
        self.assertEqual(self.library.library_name, test_name)

class Test_Fund_Library(unittest.TestCase):

    def setUp(self):
        self.fund_library = Fund_Library("Fund of rare and valuable publications", "City Library №1", 32, 7, 44, 15, 3, 11)

    def test_fund_change_number_books(self):
        test_number_books = 34
        self.fund_library.change_number_books(34)
        self.assertEqual(self.fund_library.number_books, test_number_books)

class Test_Literature_Type(unittest.TestCase):

    def setUp(self):
        self.literature_type = Literature_Type("publication")

    def test_rename_literature_type(self):
        test_literature_type_name = "book"
        self.literature_type.rename_literature_type("book")
        self.assertEqual(self.literature_type.literature_type_name, test_literature_type_name)

class Test_Worker(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Ivanov", "City Library №1", "librarian", 1997, 2019, "complete secondary educaton", 14500)

    def test_worker_change_salary(self):
        test_salary = 16000
        self.worker.change_salary(16000)
        self.assertEqual(self.worker.salary, test_salary)

class Test_Fund_Replenishment(unittest.TestCase):

    def setUp(self):
        self.fund_replenishment = Fund_Replenishment("Fund of rare and valuable publication", "Ivanov", "06.12.2022",
                                                     "City Library №3", "book", "Эксмо", "12.03.2012", 50)

    def test_fund_replenishment_increase_number_copies_on(self):
        test_number_copies = 60
        self.fund_replenishment.increase_number_copies_on(10)
        self.assertEqual(self.fund_replenishment.number_copies, test_number_copies)


if __name__ == '__main__':
    unittest.main()
