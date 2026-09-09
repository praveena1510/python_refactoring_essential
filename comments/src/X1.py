class X1:

    @staticmethod
    def sum_of_squares_in_range(lower_bound, upper_bound):
        accumulated_sum = 0

        # Iterate from lower bound (q) to upper bound (z)
        for i in range(lower_bound, upper_bound + 1):
            # Add square of each number in the range
            accumulated_sum += X1.n(i)

        # Return accumulated sum
        return accumulated_sum

    @staticmethod
    def n(k):
        # Return square of input
        return k * k