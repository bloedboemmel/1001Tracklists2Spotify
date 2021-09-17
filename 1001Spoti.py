from tracklists import *
import base64
from google_images_download import google_images_download
import spotipy
from spotipy import SpotifyOAuth
from keys import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def add():

    tl = Tracklist(url)
    name = tl.title
    

    tracks = tl.tracks
    
    uris = []
    for track in tracks:
        if track.title == "ID" or track.full_artist == "ID":
            continue
        song = track.title + ' ' + track.artist.name.split('&')[0]
        s = spotify.search(song, 25)

        if len(s['tracks']['items']) == 0:
            print(f"{bcolors.WARNING} Nothing found for {track.title} by {track.full_artist}! {bcolors.ENDC}")
        else:
            uris.append(s['tracks']['items'][0]['uri'])

    #for uri in uris:
        #print(uri)


    print(f"{bcolors.OKGREEN} Found: {len(uris)} of IDed {tl.num_tracks_IDed} of total {tl.num_tracks} {bcolors.ENDC}")
    d = 99
    pl = spotify.user_playlist_create(user_id, name, public=True, description=f"Unofficial tracklist of {name}. Automatically created by https://github.com/bloedboemmel/")
    
    playlist = pl['uri']
    SONGS2 = [uris[i:i + d] for i in range(0, len(uris), d)]
    for songs in SONGS2:
        spotify.playlist_add_items(playlist, songs)
    
    
    try:
        imagepath = google(name)
        print(imagepath)
        with open(imagepath, "rb") as img_file:
            img = base64.b64encode(img_file.read()).decode('utf-8')
            spotify.playlist_upload_cover_image(playlist, image_b64=img)
    except:
        print("{bcolors.WARNING} No playlist-picture set {bcolors.ENDC}")
    
    print(f"{bcolors.OKBLUE} Finished! You can find the playlist at {pl['external_urls']['spotify']} {bcolors.ENDC}")

def google(name):
    search = f"{name.replace(',', '').replace('ö','o').replace('|','')}"
      # importing the library

    response = google_images_download.googleimagesdownload()  

    arguments = {"keywords": f"{search}", "limit": 1,
                 "print_urls": True, "a": "square", "no_directory": True} 
    paths = response.download(arguments) 
      
    print(paths[0])
    return paths[0][f"{search}"][0]


if __name__ == '__main__':
    url = input("Tracklist1001-URL: ")
    client_id, client_secret, redirect_uri, scope, user_id = spotify_keys()
    spotify = spotipy.Spotify(
        auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                                  scope=scope, open_browser=False))
    
    add()
    