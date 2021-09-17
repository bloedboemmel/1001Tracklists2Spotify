client_id = 'YOUR SPOTIFY CLIENT ID'
client_secret = 'YOUR SPOTIFY CLIENT SECRET'
redirect_uri = 'http://localhost' #your redirect uri
user_id = 'your username'
scope = 'ugc-image-upload user-read-recently-played user-top-read user-read-playback-position user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-modify-public playlist-modify-private  playlist-read-collaborative user-follow-modify user-follow-read user-library-modify user-library-read user-read-email user-read-private' # your scopes

def spotify_keys():
    return client_id, client_secret, redirect_uri, scope, user_id