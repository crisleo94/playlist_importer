# Playlist Importer
<img src="https://img.shields.io/github/issues/crisleo94/playlist_importer"> <img src="https://img.shields.io/github/stars/crisleo94/playlist_importer"> <img src="https://img.shields.io/github/license/crisleo94/playlist_importer">

# Index
The main idea behind this python script is to achieve a sort of automation related to exporting/importing playlists in YoutubeMusic or Spotify, for example if I have a 500 songs in a Spotify playlist and want that same playlist in my Youtube, I won't start adding the song one by one, so this is why this application was born. After reading both Spotify API and Youtube API documentation the best way to go is to create an API connected with a frontend

# Tasks
- [x] Create Flask application
- [ ] Create routes for the application
- [ ] Create frontend in react to consume this API
- [x] Create Spotify Application
- [ ] Create Application in google developers console
- [x] Create .env file to store the client and client secret ID's
- [ ] Use [python-dotenv](https://pypi.org/project/python-dotenv/) to get the ID's from the .env file
- [ ] Use [requests](https://pypi.org/project/requests/) to start making the requests to the provided endpoint by spotify and youtube music
- [ ] Obtain a list with the playlists from Spotify/Youtube

# LICENSE
MIT