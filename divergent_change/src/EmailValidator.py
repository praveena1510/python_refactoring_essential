import re


class EmailValidator:

    def is_valid_email(self, email: str) -> bool:
        if email is None:
            return False
        pattern = r"^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"
        return re.match(pattern, email) is not None
