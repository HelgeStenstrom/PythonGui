# Translation to Python from https://martinfowler.com/articles/mocksArentStubs.html

import warehouse as w

import unittest
from unittest.mock import MagicMock

TALISKER = "Talisker"
HIGHLAND_PARK = "Highland Park"

class OrderStateTests(unittest.TestCase):

    def __init__(self, args):
        super().__init__(args)
        #self.TALISKER = "Talisker"
        #self.HIGHLAND_PARK = "Highland Park"
        self.warehouse = w.WarehouseImpl()


    def setUp(self):
        self.warehouse.add(TALISKER, 50)
        self.warehouse.add(HIGHLAND_PARK, 25)

    def test_order_is_filled_if_enough_in_warehouse(self):
        order = w.Order(TALISKER, 50)
        order.fill(self.warehouse)
        self.assertTrue(order.isFilled())
        self.assertEqual(0, self.warehouse.getInventory(TALISKER))

    @unittest.skip
    def test_order_does_not_remove_if_not_enough(self):
        order = w.Order(TALISKER, 51)
        order.fill(self.warehouse)
        self.assertFalse(order.isFilled())
        self.assertEqual(50, self.warehouse.getInventory(TALISKER))


class OrderInteractionTester(unittest.TestCase):
    pass

    def   testFillingRemovesInventoryIfInStock(self):
        # setup - data
        order =  w.Order(TALISKER, 50)
        # warehouseMock =  Mock(Warehouse.class);

        wh = w.WarehouseImpl()


        # setup expectations

        # exercise
        order.filled(wh)

        # verify





