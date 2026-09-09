class NameFormatter:

    def format_display_name(self, first_name: str, last_name: str) -> str:
        return f"{first_name.strip()} {last_name.strip().upper()}"
