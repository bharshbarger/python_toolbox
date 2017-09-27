import re


def validate_ip_address(self,ip):
    ip_address_regex=re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")

    if ip_address_regex.match(ip):
        return True
    else
        return False

