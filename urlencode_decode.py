import urllib.parse


urllib.parse.quote("asd")
# 'asd'

urllib.parse.quote("asd{asd}")
# 'asd%7Basd%7D'

urllib.parse.unquote("asd{asd}")
# 'asd{asd}'

urllib.parse.unquote("asd%7Basd%7D")
# 'asd{asd}'


print(urllib.parse.quote('{"action":"get_wx_message_body", "edata"="213"}'))
