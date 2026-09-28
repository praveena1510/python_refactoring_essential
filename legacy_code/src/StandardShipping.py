class StandardShipping:

    def calculate_shipping_for_type(self, order):
        return order.weightKg * 0.5
