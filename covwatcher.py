#!/usr/bin/python3
import subprocess
import time
import os

ptoday = 0

while True:
    try:
        proc = subprocess.Popen(['/root/bin/covdaily'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = proc.communicate()[0].decode('utf-8').splitlines()

        today = int(data[0])

        if not today == ptoday:
            diffstr = f'US Cases today: {today} (+{str(today - ptoday)})'
            totalstr = f'US Cases yesterday: {int(data[1])}'
            # os.system('notify-send \'COVID Update\' \'Cases Today: ' + str(data[0]) + f" {diffstr} \' --icon=dialog-information")
            os.system(f'notify-send \'COVID Update\' \'{diffstr}\n{totalstr}\' --icon=dialog-information -t 12000')

        ptoday = today

    except:
        print('Error occurred, trying again soon')

    time.sleep(120)
