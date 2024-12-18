''' # Donnée API #
Consumer Key 	amtStcrgKGmQFzHJvubE
Consumer Secret 	aaQIgEAcyIXmJKiPzoQCGJJVEuYBfuth
Demander l'URL du Token 	https://api.discogs.com/oauth/request_token
Autoriser l'URL 	https://www.discogs.com/fr/oauth/authorize
URL du jeton d'accès 	https://api.discogs.com/oauth/aaQIgEAcyIXmJKiPzoQCGJJVEuYBfuth
'''
from requests_oauthlib import OAuth1Session

# Informations d'authentification OAuth
consumer_key = 'amtStcrgKGmQFzHJvubE'
consumer_secret = 'aaQIgEAcyIXmJKiPzoQCGJJVEuYBfuth'
request_token_url = 'https://api.discogs.com/oauth/request_token'
authorize_url = 'https://www.discogs.com/fr/oauth/authorize'
access_token_url = 'https://api.discogs.com/oauth/access_token'

# Création de la session OAuth
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='oob')

# Obtenir le jeton de demande
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

# Direct the user to the authorization URL
authorization_url = oauth.authorization_url(authorize_url)
print('Please go here and authorize:', authorization_url)
verifier = input('Paste the PIN here: ')

# Obtenir le jeton d'accès
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)
access_token = oauth_tokens['oauth_token']
access_token_secret = oauth_tokens['oauth_token_secret']