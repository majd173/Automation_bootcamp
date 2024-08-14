import unittest
from sqlalchemy import create_engine
from data_base_projects.users_example.models import Base, Users
from sqlalchemy.orm import sessionmaker


class TestUser(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.user_one = Users(name='positive', email='test@email.com')
        self.session.add(self.user_one)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()
    def test_user_exist_by_name(self):
        user_from_table = self.session.query(Users).filter_by(name=self.user_one.name).first()
        self.assertIsNotNone(user_from_table)
        self.assertEqual(user_from_table.email, self.user_one.email)

    def test_user_exist_by_email(self):
        user_from_table = self.session.query(Users).filter_by(email=self.user_one.email).first()
        self.assertIsNotNone(user_from_table)
        self.assertEqual(user_from_table.name, self.user_one.name)
