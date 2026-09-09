from divergent_change.src.AccountStatusDeterminer import AccountStatusDeterminer
from divergent_change.src.EmailValidator import EmailValidator
from divergent_change.src.LoyaltyPointsCalculator import LoyaltyPointsCalculator
from divergent_change.src.NameFormatter import NameFormatter


class CustomerService:

    def __init__(self, email_validator: EmailValidator):
        self.email_validator = email_validator
        self.name_formatter = NameFormatter()
        self.loyalty_points_calculator = LoyaltyPointsCalculator()
        self.account_status_determiner = AccountStatusDeterminer()

    def is_valid_email(self, email: str) -> bool:
        return self.email_validator.is_valid_email(email)

    def format_display_name(self, first_name: str, last_name: str) -> str:
        return self.name_formatter.format_display_name(first_name, last_name)

    def calculate_loyalty_points(self, number_of_purchases: int) -> int:
        return self.loyalty_points_calculator.calculate_loyalty_points(number_of_purchases)

    def determine_account_status(self, days_since_last_login: int) -> str:
        return self.account_status_determiner.determine_account_status(days_since_last_login)


