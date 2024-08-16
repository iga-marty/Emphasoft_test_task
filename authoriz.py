from rauth import OAuth2Service

github = OAuth2Service(
    name="github",
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "user:email"})

redirect_uri = 'https://github.com/login/oauth/authorize'
params = {'scope': 'read_stream',
          'response_type': 'code',
          'redirect_uri': redirect_uri}

url = facebook.get_authorize_url(**params)

session = facebook.get_auth_session(data={'code': 'foo',
                                           'redirect_uri': redirect_uri})

print(session.get('me').json()['username'])