# ApkPure Api Enpoint ✨
Search, Simplify detail & Downloadable from Apkpure.com

[![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7-brightgreen.svg)](pytho.org) 
[![License](https://img.shields.io/badge/MIT-License-blue.svg)](https://opensource.org/licenses/MIT)
___
## Features
1. Simply to use
2. Readable
3. Using async request & multithreading for really fast request (not really sure)
4. Easy accessing dictionary

## Installing
- `git clone https://github.com/kurodenjiro/api.apkpure`
- `cd api.apkpure`
- `pip3 install -r requirements.txt`

## Start Server
```python
python3 main.py
```
## API document
### Search
```Http
GET localhost:5000/query?search=<query string>
```

### Get Detail
```Http
GET http://localhost:5000/app?url=<url app> 
example : http://localhost:5000/app?url=/pubg-tencent-1i/com.tencent.ig
```
### Get Trending
```Http
GET http://localhost:5000/trending
```

## How to
```python
from apis import ApkPure

apk = ApkPure(return_as="dict")
#set 'dict' or 'rpc' for returning as
```
### Search Application
```python
search = api._search("pubg")
print(search)
```

### Get Details from giving url
```python
details = api.detail_from_url(search.results[0].url)
print(details)

# or you can get position of array when return data
search = api._search("pubg")
detail = api._detail(search, 1)
print(detail)
```
### Get Trending
```python
trending = api._trending()
print(trending)
```

### Download application
```python
api._download(url=detail.url_download, name=detail.title, ex=detail.extension, path="/downloads)
```



# Author
Kuro / [Kuro](https://github.com/kurodenjiro/api.apkpure)
=======
# api.apkpure
