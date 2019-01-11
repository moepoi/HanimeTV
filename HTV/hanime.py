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
        self.host = "https://hanime.tv"
        if email is None and password is None:
            self.session = ''
        else:
            try:
                login = self.login(email, password)
                self.session = login["session_token"]
            except:
                print ("Invalid Credential")
                sys.exit()

    def login(self, email, password):
        url = "{}/api/v3/sessions".format(self.host)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
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
            "password": str(password)
        }
        req = requests.post(url, headers=headers, json=data)
        return json.loads(req.text)

    def search(self, query):
        url = "https://thorin-us-east-1.searchly.com/hentai_videos/hentai_video/_search?from=0&size=48"
        token = "cHVibGljOmlscXd3a2s3Znpxb3Bzand3MXVkcm1yZHQwdDlnb2Mz"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': '{}/search?q={}'.format(self.host, str(query)),
            'Authorization': 'Basic {}'.format(str(token)),
            'content-type': 'application/json',
            'Origin': self.host,
            'Connection': 'keep-alive',
            'TE': 'Trailers'
        }
        data = {
            "query": {
                "bool": {
                    "filter": {
                        "bool": {
                            "minimum_should_match": 0,
                            "must": [
                                {
                                    "bool": {
                                        "must": []
                                    }
                                }
                            ],
                            "must_not": None,
                            "should": []
                        }
                    },
                    "minimum_should_match": 1,
                    "should": [
                        {
                            "wildcard": {
                                "name": {
                                    "boost": 10,
                                    "wildcard": "*{}*".format(str(query))
                                }
                            }
                        },
                        {
                            "match": {
                                "titles": "{}".format(str(query))
                            }
                        },
                        {
                            "wildcard": {
                                "tags_string": "{}*".format(str(query))
                            }
                        }
                    ]
                }
            },
            "sort": [
                "_score",
                {
                    "created_at_unix": {
                        "order": "desc"
                    }
                }
            ]
        }
        req = requests.post(url, headers=headers, json=data)
        return json.loads(req.text)

    def get(self, url):
        query = url.replace("https://hanime.tv/hentai-videos/","")
        url = "https://hanime.tv/api/v5/videos_manifests/" + query
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
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