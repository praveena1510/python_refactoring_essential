class RangeCalculator:

    @staticmethod
    def sum_of_squares_in_range(lower_bound, upper_bound):
        accumulated_sum = 0

        for i in range(lower_bound, upper_bound + 1):
            accumulated_sum += RangeCalculator.square(i)

        return accumulated_sum

    @staticmethod
    def square(input):
        return input * input