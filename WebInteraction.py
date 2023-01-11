# PYTHON WEB INTERACTION - URLLIB VS REQUESTS



URLLIB 2

----
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
gh_url = 'https://api.github.com'
req = urllib2.Request(gh_url)
password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'pass')
auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)
urllib2.install_opener(opener)
handler = urllib2.urlopen(req)
print handler.getcode()
print handler.headers.getheader('content-type')
# ------
# 200
# 'application/json'




1_requests.py
---------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
r = requests.get('https://api.github.com', auth=('user', 'pass'))
print r.status_code
print r.headers['content-type']
# ------
# 200
# 'application/json'
