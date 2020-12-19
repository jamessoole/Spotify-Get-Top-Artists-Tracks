import os
from client import SpotifyClient


# IMPORTANT - set token w/ following on cmd line
# export token=<paste token here>

# get OAUTH from https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/
# optional - env | grep token     linux keywords to check if loaded
# note - export is linux command, use 'set' for windows

# note - Tokens expire after an hour
# KeyError: 'tracks' likely caused by expired token

# current syntax for python3 (f-strings)



def run():

    # # if you'd prefer an input
    # token = input("What's your OAUTH Token? ")
    # client = SpotifyClient(token)
    client = SpotifyClient(os.getenv('token'))
    print(f"token is: {os.getenv('token')}")


    choice = input("Return top 'artists' or 'tracks'?  ")
    if not (choice == 'artists' or choice== 'tracks'):
        print("Term not recognized. Default: tracks.")
        choice = 'tracks'

    if choice == 'tracks':
        want_analysis = input("Include audio analysis (y,n)?  ")
        tracks = client.get_top_tracks()
        print()
        print('The following are your top tracks, starting with the most played')
        print()
        for i, track in enumerate(tracks):
            num = '{:<3}'.format(str(i+1)+'.')
            print(f"{num} '{track['name']}' by {track['artists'][0]['name']} ")
            if (want_analysis == 'y'):
                features = client.get_analysis(track["id"])
                print(f"energy: {features['energy']}")
                print(f"valence: {features['valence']}")
                print(f"mode: {features['mode']}")
                print(f"danceability: {features['danceability']}")
                print(f"tempo: {features['tempo']}")
                print()



    if choice == 'artists':
        want_details = input("Include audio analysis (y,n)?  ")
        artists = client.get_top_artists()
        print()
        print('The following are your top artists, starting with the most played')
        print()
        for i,artist in enumerate(artists):
            num = '{:<3}'.format(str(i+1)+'.')
            print(f"{num} {artist['name']} ")
            if (want_details == 'y'):
                details = client.get_artist_details(artist["id"])
                print(f"main genre: {details['genres'][0]}")
                print(f"popularity: {details['popularity']}")
                print()


    # # testing
    # for track in tracks:
    #     print(track['name'])


# if run directly
if __name__ == "__main__":
    run()