from legacy_code.src.ExpressShipping import ExpressShipping
from legacy_code.src.InternationalShipping import InternationalShipping
from legacy_code.src.OrderAPI import OrderAPI
from legacy_code.src.OvernightShipping import OvernightShipping
from legacy_code.src.StandardShipping import StandardShipping


class ShippingCalculator:

    def __init__(self, order_api: OrderAPI, shipping_types=None):
        self.order_api = order_api
        self.shipping_types = shipping_types

    def calculate_shipping(self, order_id: int) -> float:
        try:
            order = self.order_api.fetch_order_details(order_id)
            if order.shippingType in self.shipping_types:
                shipping_method = self.shipping_types[order.shippingType]
                return shipping_method.calculate_shipping_for_type(order)
            else:
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")

        except Exception as e:
            print(e)
            return -1.0
