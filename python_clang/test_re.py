"""正则"""

import re

print(re.match("ad", "adsadsad"))
print(re.match("(d)", "adsad323242sad"))
print(re.search("(d)", "adsad323242sad"))
print(re.sub(r"\D", '', "adsad323242sad"))
print(re.sub(r"\D", '', "adsasad"))
