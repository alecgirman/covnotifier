#!/usr/bin/bash
curl -s https://www.worldometers.info/coronavirus/country/us/ | rg 'USA Total' -A 2 -B 0 | rg -o '\+(\d|,)+' | sed -E 's/,|\+//g'
