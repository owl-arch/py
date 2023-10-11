##
# https://dev.to/cwprogram/python-networking-http-2o3
##

from urllib.parse import urlparse

URL = 'https://user:password@domain.com:7777/'
parsed_url = urlparse(URL)
print(parsed_url.hostname)
print(parsed_url.username)
print(parsed_url.password)
print(parsed_url.port)

# Output:
# domain.com
# user
# password
# 7777


from urllib.parse import quote

print(quote('/path with spaces'))

# Output:
# /path%20with%20spaces