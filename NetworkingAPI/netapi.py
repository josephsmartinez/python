import requests
import urllib

from rfc3986 import builder

# datetime-to-rfc-2822
import datetime
import time
from email import utils
# Keyed-Hashing for Message Authentication
import hmac
import hashlib


nowdt = datetime.datetime.now()
nowtuple = nowdt.timetuple()
nowtimestamp = time.mktime(nowtuple)
print(utils.formatdate(nowtimestamp))

date = utils.formatdate(nowtimestamp)
host = "api.hav.edu"
uri = "/v1/mac/"
username = "cheese"
method = "GET"
password = "QzY0Q0EzVBRkJCMERDOEUyCg"
mac = "78:24:af:3a:27:ea"

rfc3986_uri = ""

# Array ( [0] => Fri, 01 Feb 2019 02:32:34 +0000 [1] => GET [2] => api.fiu.edu [3] => /v1/mac/78:24:af:3a:27:ea [4] => method=GET&uri=%2Fv1%2Fmac%2F78%3A24%3Aaf%3A3a%3A27%3Aea ) 
# 591fb57dcc7508ff516cbbe5f41f77392392e8ce

# method=GET&uri=%2Fv1%2Fmac%2F78%3A24%3Aaf%3A3a%3A27%3Aea
# method=GET&uri=%2Fv1%2Fmac%2F78%3A24%3Aaf%3A3a%3A27%3Aea

# Build a URL that looks like the rquivalent
# Example: api.fiu.edu&/v1/mac78:24:af:3a:27:ea/&PHP_QUERY_RFC3986   

#http_build_query = builder.URIBuilder().add_host(url).add_path(uri).finalize().unsplit() 
#http_build_query = builder.URIBuilder(scheme=None, userinfo=None, host=host, port=None,path=uri, query=None, fragment=None).finalize().unsplit()

# Implementation of RFC 3986 
rfc3986_uri = builder.URIBuilder().add_query_from([('method', 'GET'), ('uri',uri + mac)]).finalize().unsplit()
print(rfc3986_uri) # FIXME remove (?) from string 


# Create the signed message from api key and string to sign
password = hmac.new('pass'.encode('utf-8'), 'hello'.encode('utf-8'), hashlib.sha1).hexdigest()
print(password)

# arr = [ "Fri, 01 Feb 2019 02:32:34 +0000", "GET", "api.fiu.edu",/v1/mac/78:24:af:3a:27:ea, api.fiu.edu&/v1/mac78:24:af:3a:27:ea/&PHP_QUERY_RFC3986 ]
#hash_password = hash_hmac('sha1', implode("\n", arr), password);





# class api():
#   def __init__ = (self)
#     username = "case"
#     password = "QzY0Q0EzMkItRjcyQy00QkQwLUI4NEYtRDVBRkJCMERDOEUyCg"
  
#   def get_mac(mac):
