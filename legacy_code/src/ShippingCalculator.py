from legacy_code.src.ExpressShipping import ExpressShipping
from legacy_code.src.InternationalShipping import InternationalShipping
from legacy_code.src.OrderAPI import OrderAPI
from legacy_code.src.OvernightShipping import OvernightShipping
from legacy_code.src.StandardShipping import StandardShipping


class ShippingCalculator:

    def __init__(self, order_api: OrderAPI):
        self.order_api = order_api

    def calculate_shipping(self, order_id: int) -> float:
        try:
            order = self.order_api.fetch_order_details(order_id)

            if order.shippingType == "STANDARD":
                return StandardShipping().calculate_shipping_for_type(order)

            elif order.shippingType == "EXPRESS":
                return ExpressShipping().calculate_shipping_for_type(order)

            elif order.shippingType == "OVERNIGHT":
                return OvernightShipping().calculate_shipping_for_type(order)
            elif order.shippingType == "INTERNATIONAL":
                return InternationalShipping().calculate_shipping_for_type(order)

            else:
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")

        except Exception as e:
            print(e)
            return -1.0
