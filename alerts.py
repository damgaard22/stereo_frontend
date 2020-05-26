
import csv

with open('alerts.csv') as f:
    a = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

for alert in a:
    alert['Time'] = alert['Time'].split(' ')[0]
    for k, v in alert.items():
        if '.' in v:
            alert[k] = v.replace('.', '').split(',')[0]
        elif ',' in v:
            alert[k] = v.replace(',', '.')

for alert in a:
    for k, v in alert.items():
        print(k, v)

