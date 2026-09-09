class AccountStatusDeterminer:

    def determine_account_status(self, days_since_last_login: int) -> str:
        if days_since_last_login > 365:
            return "INACTIVE"
        elif days_since_last_login > 30:
            return "DORMANT"
        return "ACTIVE"
