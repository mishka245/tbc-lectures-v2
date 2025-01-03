import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en;q=0.5',
    'authorization': 'false',
    'baggage': 'sentry-environment=production,sentry-public_key=58cee8a976517e11a3884d9f18138451,sentry-trace_id=e72194a62411408195502535ae130749,sentry-sample_rate=0.1,sentry-sampled=false',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.mymarket.ge',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.mymarket.ge/',
    'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'sentry-trace': 'e72194a62411408195502535ae130749-95e706a4b383bd65-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

data = {
    'Keyword': 'გენერატორი',
    'Limit': '28',
    'Page': '1',
    'SortID': '1',
    'WithShops': '1',
}

session = requests.Session()

session.headers = {}

response = session.post('https://api.mymarket.ge/api/ka/products', headers=headers, data=data)


print(response.status_code)
print(response.text)