import re

ip_address_regex=re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")

if ip_address_regex.match(t):
    return True
else
    return False

