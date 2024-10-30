import unittest
import logging
from api_automation_projects.pet_store.infra.config_provider import ConfigProvider
from api_automation_projects.pet_store.infra.jira_handler import JiraHandler
from api_automation_projects.pet_store.infra.utilities import Utils
from api_automation_projects.pet_store.logic.Store.store import StorePage
from api_automation_projects.pet_store.infra.api_wrapper import ApiWrapper
from api_automation_projects.pet_store.logic.entity.order_details import OrderDetails


class TestStore(unittest.TestCase):

    def setUp(self):
        # ARRANGE
        """
        Setting up URL and base details fot adding and getting a username.
        """
        self._config = ConfigProvider().load_from_file(
            r"\api_automation_projects\pet_store\pet_store.json")
        self._api = ApiWrapper()
        self._pet_store = StorePage(self._api)
        self._jira_flag = JiraHandler()
        self._order_details = OrderDetails(
            Utils.generate_random_number(2),
            Utils.generate_random_number(2),
            Utils.generate_random_number(6))
        self._order_response = self._pet_store.store_order_add(self._order_details)

    def tearDown(self):
        # self._jira_flag.create_jira_issue_teardown(
        #     self._config['jira_key'], 'test_store_order_add',
        #     'Make sure to add order to the database', 'Task')
        logging.info("_______TEST COMPLETED_______")

    # --------------------------------------------------------------------------------------

    def test_pet_store_inventory(self):
        """
        Test Case #4: Store inventory.
        Testing acceptance and status code of a request and a received body confirmation.
        """
        logging.info("4_______TEST (STORE) BEGAN_______4")
        # ACT
        inventory_response = self._pet_store.store_inventory()
        # ASSERT
        self.assertTrue(inventory_response.ok)
        self.assertEqual(self._config['status_code_passed'], inventory_response.status_code)
        self.assertIn(self._config['inventory_sold'], inventory_response.data)
        self.assertIn(self._config['inventory_available'], inventory_response.data)

    # --------------------------------------------------------------------------------------

    def test_store_order_add(self):
        """
        Test Case #5: Add an order.
        Testing acceptance and status and body information of a request after submitting a post.
        """
        logging.info("5_______TEST (STORE) BEGAN_______5")
        # ASSERT
        self.assertTrue(self._order_response.ok)
        self.assertEqual(self._config['status_code_passed'], self._order_response.status_code)
        self.assertEqual(self._order_response.data['id'], self._order_details.order_id)
        self.assertEqual(self._order_response.data['petId'], self._order_details.pet_id)
        self.assertEqual(self._order_response.data['quantity'], self._order_details.quantity)

    # --------------------------------------------------------------------------------------

    def test_store_order_get(self):
        """
        Test Case #6: Store order.
        Testing request received of an order by its id.
        """
        logging.info("6_______TEST (STORE) BEGAN_______6")
        # ACT
        get_order_response = self._pet_store.store_order_by_id(self._order_details.order_id)
        # ASSERT
        self.assertEqual(get_order_response.data["id"], self._order_details.order_id)
        self.assertEqual(get_order_response.data["petId"], self._order_details.pet_id)
        self.assertEqual(get_order_response.data["quantity"], self._order_details.quantity)


if __name__ == '__main__':
    unittest.main()
