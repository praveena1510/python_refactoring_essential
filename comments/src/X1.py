class X1:

    @staticmethod
    def m(lower_bound, z):
        p = 0

        # Iterate from lower bound (q) to upper bound (z)
        for i in range(lower_bound, z + 1):
            # Add square of each number in the range
            p += X1.n(i)

        # Return accumulated sum
        return p

    @staticmethod
    def n(k):
        # Return square of input
        return k * k