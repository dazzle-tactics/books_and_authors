import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Graham Greene")
author_repository.save(author1)
author2 = Author("Kurt Vonnegut")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("The Third Man", author1, "Thriller", 1949)
book2 = Book("Cat's Cradle", author2, "Satire", 1964)

book_repository.select_all()

pdb.set_trace()