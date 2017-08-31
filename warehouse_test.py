# Translation to Python from https://martinfowler.com/articles/mocksArentStubs.html

import warehouse as w

import unittest
from unittest.mock import MagicMock

TALISKER = "Talisker"
HIGHLAND_PARK = "Highland Park"


class OrderStateTests(unittest.TestCase):

    def __init__(self, args):
        super().__init__(args)
        self.warehouse = w.WarehouseImpl()

    def setUp(self):
        # The warehose is a collaborator.
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

    def testFillingRemovesInventoryIfInStock(self):
        # setup - data
        order = w.Order(TALISKER, 50)

        # The collaborator
        # Java:
        #  Mock warehouseMock = new Mock(Warehouse.class);
        warehouseMock = MagicMock()

        # warehouseMock =  Mock(Warehouse)
        order.fill = MagicMock(name='fill')

        # setup expectations, maybe not here in Python

        # exercise
        order.fill(warehouseMock)

        # verify
        order.fill.assert_called_once()
        # warehouseMock.

    def testFillingRemovesInventoryIfInStock_usingWith(self):
        # setup - data
        order = w.Order(TALISKER, 50)

        with unittest.mock.patch('warehouse.WarehouseImpl') as mock:
            order.fill(mock)
            pass

    @unittest.mock.patch('warehouse.WarehouseImpl')
    # TypeError: testWithDecorator() takes 1 positional argument but 2 were given
    def testWithDecorator(self, arg):
        print("testWithDecorator called with arg = ", arg)
        print("its arg has ", dir(arg))
        print("its type is", type(arg))
        self.assertEqual(arg.name, "WarehouseImpl")
        pass


class LearnPythonExample(unittest.TestCase):
    def testTheExample(self):
        barInstance = w.Bar()
        with unittest.mock.patch('warehouse.Foo') as mock:
            anInstance = mock.return_value
            anInstance.method.return_value = 'the result'
            result = barInstance.some_function()
            self.assertEqual(result, 'the result', 'return value matching')
