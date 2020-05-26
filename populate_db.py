
import csv
import datetime
from datetime import time, timedelta
import json
import os
import requests


def strategy_map(strategy):
    if strategy == 'High Momo':
        return 1


def reformat_date(date):
    return '-'.join([date.split('-')[-1]] + date.split('-')[:-1])


def reformat_gapper_date(date):
    return '-'.join(reversed(date.split('-')))


def send_to_stereo_gappers(alerts, date):
    for alert in alerts:
        for k, v in alert.items():
            if k != 'time' and '.' in v:
                alert[k] = v.replace('.', '').split(',')[0]
            elif k != 'time' and ',' in v:
                alert[k] = v.replace(',', '.')

        try:
            alert['price'] = float(alert['price'])
        except:
            alert['price'] = 0.0

        try:
            alert['float'] = int(alert['float'])
        except:
            alert['float'] = 0

        try:
            alert['volume'] = int(alert['volume'])
        except:
            alert['volume'] = 0

        try:
            alert['gap_dollars'] = float(alert['gap_dollars'])
        except:
            alert['gap_dollars'] = 0

        try:
            alert['gap_percentage'] = float(alert['gap_percentage'])
        except:
            alert['gap_percentage'] = 0

        alert['strategy'] = 4
        alert['time'] = '9:25:00'
        alert['date'] = reformat_gapper_date(date)

    for alert in alerts:
        print(alert)
        r = requests.post('http://localhost:8081/api/alerts/', json=alert)
        print(r.status_code)


def send_to_stereo_alerts(alerts):
    for alert in alerts:
        alert['time'], _, alert['date'] = alert['time'].split(' ')
        temp_time = datetime.datetime.strptime(alert['time'], "%I:%M:%S") - timedelta(hours=18)
        alert['time'] = temp_time.strftime("%H:%M:%S")
        alert['date'] = reformat_date(alert['date'])
        for k, v in alert.items():
            if k != 'time' and '.' in v:
                alert[k] = v.replace('.', '').split(',')[0]
            elif k != 'time' and ',' in v:
                alert[k] = v.replace(',', '.')

        try:
            alert['relative_volume'] = float(alert['relative_volume'])
        except:
            alert['relative_volume'] = 0.0

        try:
            alert['price'] = float(alert['price'])
        except:
            alert['price'] = 0.0

        try:
            alert['float'] = int(alert['float'])
        except:
            alert['float'] = 0

        try:
            alert['volume'] = int(alert['volume'])
        except:
            alert['volume'] = 0

        try:
            alert['change'] = float(alert['change'])
        except:
            alert['change'] = 0.0

        try:
            alert['five_min_vol'] = float(alert['5min_vol'])
        except:
            alert['five_min_vol'] = 0.0

        alert['strategy'] = 1

    for alert in alerts:
        r = requests.post('http://localhost:8081/api/alerts/', json=alert)
        print(r.status_code)


# for file in os.listdir('alerts'):
#     with open(f'gappers_stereo/{file}') as f:
#         a = [{k: v for k, v in row.items() if k not in ('range', 'st', 'strat')}
#              for row in csv.DictReader(f, skipinitialspace=True)]
#         send_to_stereo_alerts(a)

for file in os.listdir('gappers_stereo'):
    with open(f'gappers_stereo/{file}') as f:
        a = [{k: v for k, v in row.items() if k not in ('range', 'st', 'strat')}
             for row in csv.DictReader(f, skipinitialspace=True)]
        _, ending = file.split(' ')
        date = ending.split('.')[0]
        send_to_stereo_gappers(a, date)
