# Spotify Get Top Artists and Tracks

### Fetch a user's top-played artists or tracks using Spotify API.

Choice of term:
- `long` history of account
- `medium` within last 6 months
- `short` within last month

Python script `run.py` calls `client.py`

##### To Use:
- get OAUTH token [here](https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/)
- must register personal project
- set token w/ following on cmd line
- `export token=<paste token here>` on linux or `set token=<paste token here>` on windows
- optional `env | grep token` to check if token has loaded

###### Notes:
- Tokens expire after an hour
- `KeyError: 'tracks'` likely caused by expired token
- current syntax for python3 (f-strings)


