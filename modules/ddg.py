import requests
import json

def ddg(args):
    keyword = "\\" + "+".join(args[1:])
    url = "http://api.duckduckgo.com/?q={0}&kp=1&format=json&kp=1&no_redirect=1&no_html=1".format(keyword)
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)
        res = data['Redirect']
        if res != "":
            return res
        else:
            return "https://duckduckgo.com/?q=" + keyword.replace("\\","")
    else:
        return "something wrong"
