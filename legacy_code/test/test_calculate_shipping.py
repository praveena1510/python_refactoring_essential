import unittest

from legacy_code.src.OrderAPI import OrderAPI, Order
from legacy_code.src.ShippingCalculator import ShippingCalculator


class CalculateShippingTest(unittest.TestCase):

    def test_standard_shipping(self):
        stub_order_api = OrderAPI()
        stub_order_api.fetch_order_details = lambda order_id: Order(orderId=1001, shippingType="STANDARD", weightKg=5,
                                                                  distanceKm=120, fragile=False
                                            )
        shipping_calculator = ShippingCalculator(stub_order_api)
        self.assertEqual(2.5, shipping_calculator.calculate_shipping(1001))

    def test_express_shipping(self):
        stub_order_api = OrderAPI()
        stub_order_api.fetch_order_details = lambda order_id: Order(orderId=1002, shippingType="EXPRESS", weightKg=8.5,
                                                                  distanceKm=300, fragile=True
                                            )
        shipping_calculator = ShippingCalculator(stub_order_api)
        self.assertEqual(36.8, shipping_calculator.calculate_shipping(1002))

    def test_overnight_shipping(self):
        stub_order_api = OrderAPI()
        stub_order_api.fetch_order_details = lambda order_id: Order(orderId=1003, shippingType="OVERNIGHT", weightKg=2,
                                                                  distanceKm=50, fragile=False
                                            )
        shipping_calculator = ShippingCalculator(stub_order_api)
        self.assertEqual(27.4, shipping_calculator.calculate_shipping(1003))

    def test_international_shipping(self):
        stub_order_api = OrderAPI()
        stub_order_api.fetch_order_details = lambda order_id:Order(orderId=1004, shippingType="INTERNATIONAL", weightKg=2, distanceKm=1000, fragile=True)
        shipping_calculator = ShippingCalculator(stub_order_api)
        self.assertEqual(3,shipping_calculator.calculate_shipping(1004))