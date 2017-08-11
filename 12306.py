import urllib.request
import ssl
import json
from cons import cons2

ssl._create_default_https_context = ssl._create_unverified_context


def get_list():
    address = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}' \
              '&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&' \
              'purpose_codes=ADULT'.format(train_date, from_station, to_station)

    url = urllib.request.Request(address)
    url.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/45.0.2454.101 Safari/537.36')
    html = urllib.request.urlopen(url).read()
    dit = json.loads(html)
    return dit['data']['result']


# 车次3
# 出发站台6
# 到达站台7
# 出发时间8
# 到达时间9
# 历时 = 10
# 硬卧 =28
# 软卧23
# 软座 24
# 无座 26
# 高级软卧
# 硬座29
# 一等座 31
# 商务座 32
# 二等座30
# 出发日期 13

station_list = {}
station_list2 = {}
for i in cons2.split('@'):
    if i:
        temp_list = i.split('|')
        station_list[temp_list[1]] = temp_list[2]
        station_list2[temp_list[2]] = temp_list[1]

train_date = input('出发日期：')
from_station = station_list[input('出发地点：')]
to_station = station_list[input('到达地点：')]

print(train_date, from_station, to_station)

title = '{0:<12}{1:<12}{2:<12}{3:<12}{4:<12}{5:<12}{6:<12}{7:<12}{8:<12}{9:<12}{10:<12}{11:<12}{12:<12}{13:<12}'.format(
    '出发站台', '到达站台', '班次', '发车时间', '到达时间', '历时', '商务座', '一等座', '二等座', '软卧', '软座', '硬卧', '硬座', '五座')

for i in get_list():
    n = i.split('|')
    n[6] = station_list2[n[6]]
    n[7] = station_list2[n[7]]
    result = '{0:<12}{1:<12}{2:<12}{3:<12}{4:<12}{5:<12}{6:<12}{7:<12}{8:<12}{9:<12}{10:<12}{11:<12}{12:<12}{13:<12}'.format(
        n[6], n[7], n[3], n[8], n[9], n[10], n[32], n[31], n[30], n[23], n[24], n[28], n[29], n[26])
    print(title)
    print('\n')
    print(result)
    print('\n')
