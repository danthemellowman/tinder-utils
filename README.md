# tinder-utils

This is a collection of assorted utilities for Tinder that one may find useful. Note that you need to set the `FACEBOOK_TOKEN` and `FACEBOOK_ID` environment variables, as described below.

## utils

### autoliker

Game theory suggests that one should always swipe right on Tinder. This utility will swipe right on everyone within a 100-mile radius of you (given sufficient time).

This is *not* meant to be sexist or misogynist. This is simply meant to maximize the number of new people that you meet by taking first impressions out of the equation.

## Useful Advice

### Where do I get my Facebook auth token (facebook\_token)?

One can obtain the Facebook token by [clicking here](https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token) Once there, go to your browser's developer console, click to the Network tab, and go to the above URL again. After the second traversal, you should see two network calls on the developer console. Click the first one and look at its response headers. There should be a "location" field in the header. The value of that field should contain an auth\_token.

You should then set this as an environment variable (`export FACEBOOK_TOKEN=token_value_here`).

### Where do I get my Facebook ID?

Go to your Facebook profile, view the source code, and search for "profile\_id" to find this.

You should then set this as an environment variable (`export FACEBOOK_ID=id_value_here`).

### The autoliker stopped working. Why might this be?

So far, I've run into two cases -- you've either run out of active Tinder users within a 100-mile radius to potentially match with, or your auth token has expired. In the first case, just wait for a bit before restarting the script, or programatically change your location (to come in a future update). In the second case, just get a new auth token and set your `FACEBOOK_TOKEN` environment variable accordingly.

I'm working on adding better error handling for these cases.

## Credits

Thanks to Benjamin Coriou for his [py-tinder](https://github.com/Coriou/py-tinder) library.