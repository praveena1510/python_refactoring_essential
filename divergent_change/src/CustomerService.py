import re


class CustomerService:

    def __init__(self):
        self.email_validator = EmailValidator()
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


class EmailValidator:

    def is_valid_email(self, email: str) -> bool:
        if email is None:
            return False
        pattern = r"^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"
        return re.match(pattern, email) is not None


class NameFormatter:

    def format_display_name(self, first_name: str, last_name: str) -> str:
        return f"{first_name.strip()} {last_name.strip().upper()}"


class LoyaltyPointsCalculator:

    def calculate_loyalty_points(self, number_of_purchases: int) -> int:
        return number_of_purchases * 10


class AccountStatusDeterminer:

    def determine_account_status(self, days_since_last_login: int) -> str:
        if days_since_last_login > 365:
            return "INACTIVE"
        elif days_since_last_login > 30:
            return "DORMANT"
        return "ACTIVE"