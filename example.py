#!/usr/bin/env python

import tinder
import os

token_url = 'https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token'

fbToken = {
  # One can obtain the Facebook token by going to the URL above. Once there, go
  # to your browser's developer console, click to the Network tab, and go to the
  # above URL again. After the second traversal, you should see two network
  # calls on the developer console. Click the first one and look at its response
  # headers. There should be a "location" field in the header. The value of that
  # field should contain an auth_token.
  'facebook_token': os.environ['FACEBOOK_TOKEN'],
  # Go to your Facebook profile, view the source code, and search for
  # "profile_id" to find this.
  'facebook_id': os.environ['FACEBOOK_ID']
}

tinder = tinder.tinderClient(fbToken)
# Print profile to show that the code is working.
print tinder.get_profile()