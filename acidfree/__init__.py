__version__ = '0.0.1'

import requests
from waitress import serve

import requests

from pyramid.config import Configurator
from pyramid.response import Response

def process_instagram_oauth(request):
    oauth_code = request.params.get('code')
    oauth_resp = requests.post(Instagram.token_point,
                  {'client_id': Instagram.client_id,
                   'client_secret': Instagram.client_secret,
                   'grant_type': 'authorization_code',
                   'redirect_uri': Instagram.redirect_uri,
                   'code': oauth_code,
                   })
    token = oauth_resp.json()['access_token']
    return Response('token: ' + token)

def create_app():
    config = Configurator()
    config.add_route('instagram', '/instagram')
    config.add_view(process_instagram_oauth, route_name='instagram')

    app = config.make_wsgi_app()
    return app


class Instagram(object):
    client_id = "8fd55323855c4a489e021edb391b911d"
    client_secret = "4e95e4e07be14373a8d9b2090e2f9d2a"
    redirect_uri = "http://localhost:9845/instagram"
    token_point = "https://api.instagram.com/oauth/access_token"
    url_template = "https://api.instagram.com/oauth/authorize/?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"

    def get_token(self):
        url = self.url_template.format(redirect_uri=self.redirect_uri,
                                  client_id=self.client_id)
        print(url)
        
    
    def recent_images(self):
        token = self.get_token()

def main():
    insta = Instagram()
    recent_instagrams = insta.recent_images()
    
    app = create_app()
    serve(app, port=9845)
    