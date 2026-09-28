class ExpressShipping:

    def calculate_shipping_for_type(self, order):
        return order.weightKg * 0.8 + order.distanceKm * 0.1