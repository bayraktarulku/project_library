from sqlalchemy import Column,  Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import create_engine
# from config import SQLALCHEMY_DATABASE_URI
SQLALCHEMY_DATABASE_URI = 'postgresql://projectlibrary:12345678@localhost/projectlibrary'

Base = declarative_base()


class Login(Base):
    __tablename__ = 'login'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255), unique=True)
    is_active = Column(Boolean())
    is_admin = Column(Integer)
    confirmed_at = Column(DateTime())

    @property
    def user_notes(self):
        return [note.note for note in self.usernotes]

    def to_dict(self):

        return {'id': self.id,
                'username': self.username,
                'email': self.email,
                'is_admin': self.is_admin,
                'confirmed_at': str(self.confirmed_at),
                'is_active': self.is_active}


class Types(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def to_dict(self):

        return {'id': self.id,
                'name': self.name}


class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    surname = Column(String(64))

    def to_dict(self):

        return {'id': self.id,
                'name': self.name,
                'surname': self.surname}


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    type_id = Column(Integer, ForeignKey('types.id'))
    type_ = relationship('Types', backref='types',
                         cascade='delete-orphan, delete', single_parent=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Authors', backref='authors',
                          cascade='delete-orphan, delete', single_parent=True)
    book_translator = Column(String(64))

    # @property
    # def book_notes(self):
    #     return [note.note for note in self.booknotes]

    def to_dict(self):

        return {'id': self.id,
                'types_id': self.types_id,
                'name': self.name,
                'author_id': self.author_id,
                'book_translator': self.book_translator,
                'notes': [n.id for n in self.book_notes]}


class Notes(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship('Books', backref='booknotes',
                        cascade='delete-orphan, delete', single_parent=True)
    text = Column(String(250))
    user_id = Column(Integer, ForeignKey('login.id'))
    user = relationship('Login', backref='usernotes',
                        cascade='delete-orphan, delete', single_parent=True)

    # def to_dict(self):

    #     return {'id': self.id,
    #             'title': self.title,
    #             'text': self.text,
    #             'book_id': self.book_id,
    #             'user': self.user_id}


engine = create_engine(SQLALCHEMY_DATABASE_URI)
DBSession = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine
Base.metadata.create_all(engine)
