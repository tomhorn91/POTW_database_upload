import requests

cookies = {
    'OptanonAlertBoxClosed': '2022-03-25T17:42:28.177Z',
    '41e4c95d7c759d614046ee36c27d0981': '9e707e27cfad4245cb50bbd5c95c85eb',
    'cb-enabled': 'enabled',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+Mar+28+2022+12%3A41%3A09+GMT-0400+(Eastern+Daylight+Time)&version=6.30.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1&geolocation=US%3BGA&AwaitingReconsent=false',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'Origin': 'https://gepir.gs1.org',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://gepir.gs1.org/index.php/search-by-gtin',
    'Accept-Language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'OptanonAlertBoxClosed=2022-03-25T17:42:28.177Z; 41e4c95d7c759d614046ee36c27d0981=9e707e27cfad4245cb50bbd5c95c85eb; cb-enabled=enabled; OptanonConsent=isIABGlobal=false&datestamp=Mon+Mar+28+2022+12%3A41%3A09+GMT-0400+(Eastern+Daylight+Time)&version=6.30.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1&geolocation=US%3BGA&AwaitingReconsent=false',
}

params = {
    'option': 'com_gepir4ui',
    'view': 'getkeylicensee',
    'format': 'raw',
}

data = {
    'keyValue': '048001014329',
    'requestTradeItemType': 'ownership',
    '6107f63c767f197c9869493bc2b17dfd': '1',
    'keyCode': 'gtin',
}

response = requests.post('https://gepir.gs1.org/index.php', headers=headers, params=params, cookies=cookies, data=data)

