#!/usr/bin/env python

import os
import sys
import tinder

fbToken = {
  'facebook_token': os.environ['FACEBOOK_TOKEN'],
  'facebook_id': os.environ['FACEBOOK_ID']
}

tinder = tinder.tinderClient(fbToken)

lat = sys.argv[1]
lon = sys.argv[2]
print tinder.updateLocation(lat, lon)