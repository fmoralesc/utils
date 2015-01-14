#!/usr/bin/python

import time
from subprocess import check_call

NOISE_TYPE = 'whitenoise'
PLAY_MINS = "20"
REST_MINS = 5

while True:
    try:
        check_call(['play', '-n', 'synth', '00:'+PLAY_MINS+':00', NOISE_TYPE])
    except:
        pass
    time.sleep(REST_MINS*60)
