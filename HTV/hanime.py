import requests
import sys

try:
    import ujson as json
except:
    import json

'''
Author : Moe Poi <moepoi@protonmail.com>
License MIT
'''

class HanimeTV:
    def __init__(self, email=None, password=None):
        self.host = "https://members.hanime.tv"
        if email is None and password is None:
            self.session = ''
        else:
            try:
                login = self.login(email, password)
                self.session = login["session_token"]
            except:
                print ("Invalid Credential")
                sys.exit()

    def pre_session(captcha_token):
        url = self.host + "/api/v1/pre-session"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
        }
        data = {
            "captcha_token": captcha_token
        }
        req = requests.post(url, headers=headers, json=data)
        return json.loads(req.text)

    def login(self, email, password):
        url = self.host + "/api/v3/sessions"
        captcha_token = "???" # NEED CAPTCHA TOKEN
        pre_session = self.pre_session(captcha_token)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': '{}/'.format(self.host),
            'Content-Type': 'application/json;charset=utf-8',
            'X-Directive': 'api',
            'Connection': 'keep-alive',
            'TE': 'Trailers'
        }
        data = {
            "email": str(email),
            "password": str(password),
            "now": pre_session["now"],
            "sign_in_token": pre_session["sign_in_token"]
        }
        req = requests.post(url, headers=headers, json=data)
        return json.loads(req.text)

    def search(self, query):
        url = "https://search.hanime.tv/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'content-type': 'application/json',
            'Origin': self.host,
            'Connection': 'keep-alive',
            'TE': 'Trailers'
        }
        data = {
            "search_text": str(query),
            "tags": [],
            "tags_mode": "OR",
            "brands": [],
            "blacklist": [],
            "order_by": "created_at_unix",
            "ordering": "desc",
            "page": 0
        }
        req = requests.post(url, headers=headers, json=data)
        return json.loads(req.text)

    def info(self, url):
        query = url.split("/")[4]
        url = self.host + "/api/v5/hentai-videos/" + query
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': '{}/hentai-videos/{}'.format(self.host, query),
            'X-Directive': 'api',
            'X-Session-Token': self.session,
            'Connection': 'keep-alive',
            'TE': 'Trailers'
        }
        req = requests.get(url, headers=headers)
        return json.loads(req.text)

    def storyboards(self, url):
        hid = self.info(url)["hentai_video"]["id"]
        url = self.host + "/api/v1/hentai_video_storyboards?hv_id={}".format(str(hid))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Session-Token': self.session,
            'Connection': 'keep-alive',
            'TE': 'Trailers'
        }
        req = requests.get(url, headers=headers)
        return json.loads(req.text)

    def download(self, url):
        url = self.host + "/api/v1/downloads/" + url.split("/")[4]
        captcha_token = "???" # NEED CAPTCHA TOKEN
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Directive': 'api',
            'X-Session-Token': self.session,
            'Connection': 'keep-alive',
            'TE': 'Trailers'
        }
        data = {
            "auth_kind": "recaptcha",
            "auth": captcha_token
        }
        req = requests.post(url, headers=headers, json=data)
        return json.loads(req.text)