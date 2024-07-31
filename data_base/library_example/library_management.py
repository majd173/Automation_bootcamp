from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine is the connection between database and python code.
engine = create_engine(r'sqlite:///C:\Users\Admin\Desktop\Automation_bootcamp\data_base\library_database.db', echo=True)

# Create table
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(Integer)


# Create table in memory
Base.metadata.create_all(engine)

# Add data to table
Session = sessionmaker(bind=engine)
session = Session()
try:
    session.query(Book).delete()
    session.commit()

    # Add data to table.
    book_one = Book(id=1, title='A good life', author='author_one', publication_date=1999)
    book_two = Book(id=2, title='Smile even its impossible', author='author_two', publication_date=2005)
    book_three = Book(id=3, title='The wide space', author='author_three', publication_date=2010)

    session.add_all([book_one, book_two, book_three])
    session.commit()

    books = session.query(Book).all()
    for book in books:
        print(f'Book: {book.title}, written by: {book.author}, was published in year {book.publication_date}')

except Exception as e:
    session.rollback()
    print(f'An error occurred: {e}')

finally:
    session.close()

