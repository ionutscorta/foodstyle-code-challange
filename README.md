# foodstyle-code-challange

Prerequirements:
apt-get install mongodb

Run api.py

In order to use the REST methods an api key needs to be generated by running a GET request on route /generateApiKey.
NOTE: For security reasons this function can only be executed from the host machine.

Using the API key generated, authenticate by calling /auth with the header Authorization: "JWT <API_KEY>"
