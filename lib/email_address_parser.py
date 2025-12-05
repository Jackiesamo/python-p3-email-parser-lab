
# email_address_parser.py
import re

class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        # Find all emails in the text
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", self.text)
        # Return sorted list alphabetically
        return sorted(emails)