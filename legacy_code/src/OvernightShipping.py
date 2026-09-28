class OvernightShipping:

    def calculate_shipping_for_type(self, order):
        return order.weightKg * 1.2 + 25
