class Library():
    
    def __init__(self, library_name, adress, city):
        self.library_name = library_name
        self.adress = adress
        self.city = city
    
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

class Literature_Type():
    
    def __init__(self, literature_type_name):
        self.literature_type_name = literature_type_name

class Worker():
    
    def __init__(self, worker_surname, library, post, year_birth, year_admission, education, salary):
        self.worker_surname = worker_surname
        self.library = library
        self.post = post
        self.year_birth = year_birth
        self.year_admission = year_admission
        self.education = education
        self.salary = salary


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
