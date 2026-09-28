from legacy_code.src.OrderAPI import OrderAPI


class ShippingCalculator:

    def __init__(self, order_api: OrderAPI):
        self.order_api = order_api

    def calculate_shipping(self, order_id: int) -> float:
        try:
            order = self.order_api.fetch_order_details(order_id)

            if order.shippingType == "STANDARD":
                return self.calculate_shipping_for_type(order)

            elif order.shippingType == "EXPRESS":
                return order.weightKg * 0.8 + order.distanceKm * 0.1

            elif order.shippingType == "OVERNIGHT":
                return order.weightKg * 1.2 + 25
            elif order.shippingType == "INTERNATIONAL":
                return order.weightKg * 1.5

            else:
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")

        except Exception as e:
            print(e)
            return -1.0

    def calculate_shipping_for_type(self, order):
        return order.weightKg * 0.5
