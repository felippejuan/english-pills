import urllib.request
urls = [
    'https://www.youtube.com/watch?v=FqE43_Qc6Lg',
    'https://www.youtube.com/watch?v=Ue-jF0cEiyg'
]
for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = urllib.request.urlopen(req).read().decode('utf-8')
        if 'Video unavailable' in res or '"status":"ERROR"' in res:
            print(f'{url} -> Video is unavailable!')
        else:
            print(f'{url} -> Video seems to exist!')
    except Exception as e:
        print(f'{url} -> ERROR: {e}')
