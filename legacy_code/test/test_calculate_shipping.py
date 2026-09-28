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
