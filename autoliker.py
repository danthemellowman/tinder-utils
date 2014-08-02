#!/usr/bin/env python

import os
import tinder

fbToken = {
  'facebook_token': os.environ['FACEBOOK_TOKEN'],
  'facebook_id': os.environ['FACEBOOK_ID']
}

tinder = tinder.tinderClient(fbToken)

# Max out your distance to maximize how many people you can like.
settings = {'distance_filter': 100}
tinder.post_profile(settings)
count = 0
# TODO: error handle when your auth token expires and when you run out of
# people close by.
while True:
  try:
    # Keep getting recs, over and over
    recs = tinder.get_recs()['results']
    for rec in recs:
      name = rec['name']
      _id = rec['_id']
      tinder.get_like(_id)
      print 'Liked ' + name + '!'
      count += 1
  except KeyboardInterrupt:
    print '\nYou swiped right on ' + str(count) + ' people in this session!'
    exit(0)