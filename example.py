from HTV import HanimeTV

hentai = HanimeTV(email="EMAIL", password="PASS")
query = "Imouto Paradise"
url = "https://hanime.tv/hentai-videos/imouto-paradise-1-ep-1"

# SEARCH
search = hentai.search(query)
print (search)

# GET INFO
info = hentai.info(url)
print (info)

# GET STORYBOARDS
storyboards = hentai.storyboards(url)
print (storyboards)

# GET DOWNLOAD (USING AUTH)
download = hentai.download(url)
print (download)