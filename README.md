## Pre-requistic

A running Keycloak server. In order to setup a Keycloak server, go to https://www.keycloak.org/docs/latest/getting_started/

## Keycloak

- In the keycloak admin panel create a new realm for e.g "djangodemo".
- create new user and set the credential as well. we will use this user to login from our djangoapp.
- create a client to represent django application  for e.g "djangoapp" . Also, give the url of the django application in 'valid redirect URIs' as 'http://localhost:8000/*'. Please note that we can set as many option as we want in order to make it more secure. For this tutorial we are doing a bear minimum configuration.

## django application
Run the following 3 command in order to install the Django OIDC libraris. Note that these are python 3 libraries.
- pip install git+https://github.com/jhuapl-boss/django-oidc.git
- pip install git+https://github.com/jhuapl-boss/drf-oidc-auth.git
- pip install git+https://github.com/jhuapl-boss/boss-oidc.git (This is compatible with django version below 2.0. In order to run it with > 2.0 please go to the following link https://github.com/jhuapl-boss/boss-oidc2 )


In settings.py files change the following with your setting.
- auth_uri = "http://localhost:8080/auth/realms/[your-realm]"
- client_id = "Your Client ID" 
- public_uri = "http://localhost:8000" (Change it if your are running django app in any other port or server)
