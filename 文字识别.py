import requests
from aip import AipOcr

image = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1608026588266&di=2980f24b0fb95d9eff9a35b0383f179e&imgtype=0&src=http%3A%2F%2Fimage.biaobaiju.com%2Fuploads%2F20190928%2F19%2F1569670434-XYkmsMxKZL.jpeg').content

APP_ID = '16149264'
API_KEY = 'yxYg9r4OuAs4fYvfcl8tqCYd'
SECRET_KEY = 'yWg3KMds2muFsWs7MBSSFcgMQl8Wng4s'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)
if 'words_result' in res.keys():
    for item in res['words_result']:
        print(item['words'])

else:
    APP_ID = '11756541'
    API_KEY = '2YhkLuyQGljPUYnmi1CFgxOP'
    SECRET_KEY = '4rrHe2BF828bI8bQy6bLlx1MelXqa8Z7'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    res = client.basicGeneral(image)
    if 'words_result' in res.keys():
        for item in res['words_result']:
            print(item['words'])
    else:
        print(res)