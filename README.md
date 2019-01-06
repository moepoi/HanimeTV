# HanimeTV

*Get data from https://hanime.tv :)*

## Installation

Installation is simple. It can be installed from pip using the following command:
```sh
$ pip3 install -r requirements.txt
```

## Usage

```sh
from HTV import HanimeTV

# hentai = HanimeTV(email="EMAIL", password="PASS")
hentai = HanimeTV()

# SEARCH
search = hentai.search("Imouto Paradise")
print (search)

# GET INFO & DATA
get = hentai.get("https://hanime.tv/hentai-videos/imouto-paradise-1-ep-1")
print (get)
```

## Credit

Moe Poi ~ / [@moepoi](https://gitlab.com/moepoi)