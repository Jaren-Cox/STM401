import json
import urllib.request, urllib.parse, urllib.error
import ssl
import twurl

Twitter_URL= 'https://api.twitter.com/1.1/statuses/user_timeline.json'

ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE

while True:
    print('')
    acct= input('Enter Twitter Account: ')
    if (len(acct)< 1): break
    url= twurl.argument(Twitter_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving...', url)
    connection= urllib.request.urlopen(url, context=ctx)
    data= connection.read().decode()
    
    js= json.loads(data)
    print(json.dumps(js, indent=2))

    headers= dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('!NO STATUS FOUND!')
        s= u['status']['text']
        print(' ', s[:50])