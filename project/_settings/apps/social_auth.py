AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY = 'aIBJhfneypvjvcWvy3IkOd1r5'
TWITTER_CONSUMER_SECRET = 'eme7efb3apVjD1czlNEMXhOgCXTb0MmxSM5qJB3H1pqpzqykab'

FACEBOOK_APP_ID = '419416788253006'
FACEBOOK_API_SECRET = 'f5337f5fca320f5fe0d972bd24c043e1'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
