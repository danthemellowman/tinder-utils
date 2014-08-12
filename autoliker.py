#!/usr/bin/env python

import os
import sys
import tinder

def print_result(count):
  print 'You swiped right on ' + str(count) + ' people in this session!'

facebook_token = sys.argv[1] if len(sys.argv) == 2 else os.environ['FACEBOOK_TOKEN']

fbToken = {
  'facebook_token': facebook_token,
  'facebook_id': os.environ['FACEBOOK_ID']
}

tinder = tinder.tinderClient(fbToken)

# Max out your distance to maximize how many people you can like.
settings = {'distance_filter': 100}
tinder.post_profile(settings)
count = 0
# TODO: error handle when your auth token expires.
while True:
  try:
    # Keep getting recs, over and over
    call = tinder.get_recs()
    # You've run out of potential matches if this branch is taken.
    if 'results' not in call:
      print_result(count)
      exit(0)
      
    recs = call['results']
    for rec in recs:
      name = rec['name']
      _id = rec['_id']
      tinder.get_like(_id)
      print 'Liked ' + name + '!'
      count += 1
  except KeyboardInterrupt:
    print_result(count)
    exit(0)
