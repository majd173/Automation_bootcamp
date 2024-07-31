import unittest
from sqlalchemy import create_engine
from data_base.product_example.model import Products, Base
from sqlalchemy.orm import sessionmaker


class TestUser(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.product_one = Products(id=1, name='impact driver', price=500.99)
        self.session.add(self.product_one)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.commit()
        self.session.close()

    def test_add_a_product(self):
        product_from_table = (self.session.query(Products).
                              filter_by(id=self.product_one.id).first())
        self.assertEqual(product_from_table.name, self.product_one.name)
        self.assertIsNotNone(product_from_table)

    def test_reading_a_product(self):
        all_products = self.session.query(Products).all()
        self.assertIn(self.product_one, all_products)

    def test_update_a_product(self):
        self.product_one.name = 'milwaukee impact driver'
        self.product_one.price = 600.99
        product_from_table = (self.session.query(Products).
                              filter_by(id=self.product_one.id).first())
        self.assertEqual(product_from_table.name, self.product_one.name)
        self.assertEqual(product_from_table.price, self.product_one.price)

    def test_remove_a_product(self):
        product_from_table = (self.session.query(Products).
                              filter_by(id=self.product_one.id).first())
        self.session.delete(product_from_table)
        all_products = self.session.query(Products).all()
        self.assertEqual(len(all_products), 0)
