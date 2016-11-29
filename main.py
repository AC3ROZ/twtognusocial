# coding: utf-8
import requests
from requests_oauthlib import OAuth1Session, OAuth1
from urllib.parse import urlparse
from os import environ
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

TWITTER_CK = environ.get('TWITTER_CK')
TWITTER_CS = environ.get('TWITTER_CS')
TWITTER_AT = environ.get('TWITTER_AT')
TWITTER_AS = environ.get('TWITTER_AS')

GNUSOCIAL_CK = environ.get('GNUSOCIAL_CK')
GNUSOCIAL_CS = environ.get('GNUSOCIAL_CS')
GNUSOCIAL_AT = environ.get('GNUSOCIAL_AT')
GNUSOCIAL_AS = environ.get('GNUSOCIAL_AS')
gnu_social = OAuth1Session(GNUSOCIAL_CK, GNUSOCIAL_CS,
                           GNUSOCIAL_AT, GNUSOCIAL_AS)
post_url = 'https://freezepeach.xyz/api/statuses/update.json'


def gnu_social_post(text):
    gnu_social.post(post_url, params={'status': text})


class GnuSocialOutListener(StreamListener):

    def on_status(self, status):
        print(type(status))
        print(status)
        if status.in_reply_to_status_id is None:
            if status.user.id == 1477133816:
                try:
                    gnu_social_post(status.text)
                except Exception as e:
                    print(e)
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    l = GnuSocialOutListener()
    auth = OAuthHandler(TWITTER_CK, TWITTER_CS)
    auth.set_access_token(TWITTER_AT, TWITTER_AS)

    stream = Stream(auth, l)
    stream.userstream()
