import requests
from bs4 import BeautifulSoup


def download(audio_url, filename):

    response = requests.get(audio_url)

    if response.status_code == 200:
        with open(f"{filename}.mp3", "wb") as file:
            file.write(response.content)
        print("Audio file downloaded successfully!")
    else:
        print("Failed to download the audio file.")

def download_recordings(url):

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        recordings = data['recordings']

        for current, recording in enumerate(recordings):
            print(f" ({current + 1}/{len(recordings)}) Downloading: {recording['file-name']}")
            download(recording['file'], recording['file-name'])
        
        print('Batch Downloading Done.')
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")



species_name = input("Species Name: ")
print(species_name)
query = species_name.replace(' ', '+')
download_recordings(f'https://xeno-canto.org/api/2/recordings?query={query}')










