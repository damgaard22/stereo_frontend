import csv
import os


def ti_to_rep_alerts(filename):
    f = open(f'alerts/{filename}', 'r')
    lines = f.readlines()
    lines[0] = lines[0] \
#       .replace('"Time"', '"time"') \
#       .replace('Price ($) [Price]', 'price') \
#       .replace("Volume Today (Shares) [TV]", 'volume') \
#       .replace('Float (Shares) [Float]', 'float') \
#       .replace('Symbol', 'symbol') \
#       .replace('Volume 5 Minute (%) [Vol5]', '5min_vol') \
#       .replace('StockTwits Relative Activity (%) [STP]', 'st') \
#       .replace('Change from the Close (%) [FCP]', 'change') \
#       .replace("Today's Range (%) [TRangeP]", 'range') \
#       .replace("Relative Volume (Ratio) [RV]", 'relative_volume') \
#       .replace("Strategy Name []", 'strat')

    #
    # f = open(f'alerts/{filename}_stereo', 'w')
    # f.writelines(lines)


def ti_to_rep_gappers(filename):
    f = open(f'gappers/{filename}', 'r')
    lines = f.readlines()
    lines[0] = lines[0] \
       .replace('Price ($) [Price]', 'price') \
       .replace("Volume Today (Shares) [TV]", 'volume') \
       .replace('Float (Shares) [Float]', 'float') \
       .replace('Symbol', 'symbol') \
       .replace('Gap ($) [GUD]', 'gap_dollars') \
       .replace('Gap (%) [GUP]', 'gap_percentage') \

#
    f = open(f'gappers_stereo/{filename}', 'w')
    f.writelines(lines)


for file in os.listdir('gappers'):
    with open(f'gappers/{file}') as f:
        ti_to_rep_gappers(file)

for file in os.listdir('gappers_stereo'):
    with open(f'gappers_stereo/{file}') as f:
        a = [{k: v for k, v in row.items() if k not in ('range', 'st', 'strat')}
            for row in csv.DictReader(f, skipinitialspace=True)]

        for alert in a:
            for k, v in alert.items():
                if '.' in v:
                    alert[k] = v.replace('.', '').split(',')[0]
                elif ',' in v:
                    alert[k] = v.replace(',', '.')

        print(a[0])