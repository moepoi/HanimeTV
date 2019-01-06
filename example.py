from HTV import HanimeTV

# hentai = HanimeTV(email="EMAIL", password="PASS")
hentai = HanimeTV()

# SEARCH
search = hentai.search("Imouto Paradise")
print (search)

# GET INFO & DATA
get = hentai.get("https://hanime.tv/hentai-videos/imouto-paradise-1-ep-1")
print (get)