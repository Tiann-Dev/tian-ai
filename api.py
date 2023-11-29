import requests
import json
import time
from tqdm import tqdm 
import os

def gpt():
        user = "Tiann Dev"
        prompt = input("\nMasukan Query: ")
        url = f"https://api.miftahganzz.my.id/api/ai/gpt-4?q={prompt}&user={user}&apikey=skynkt"
        response = requests.get(url)

        if response.status_code == 200:
                data = response.json()
                print("Response: ", data['respon'])
        else:
                print(f"Error: {response.status_code}")
                print(response.text)
def cek_ml():
        prompt = input("Input ID Game: ")
        prompt2 = input("Input ID Server: ")
        url = f"https://api.miftahganzz.my.id/api/stalking/ml?id={prompt}&zoneId={prompt2}&apikey=skynkt"
        response = requests.get(url)

        if response.status_code == 200:
                data = response.json()
                print("Response: ", data['data']['userName'])
        else:
                print(f"Error: {response.status_code}")
                print(response.text)
def down_yt():
    try:
        hu = input("  Masukan URL: ")
        api_url = "https://api.miftahganzz.my.id/api/download/youtube-video"
        api_key = "skynkt"

        url = f"{api_url}?url={hu}&apikey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            video_url = data['data']['url']
            print("  Judul: ", data['data']['title'])
            print("  Thumbnail: ", data['data']['thumb'])
            print("  Channel: ", data['data']['channel'])
            print("  Published: ", data['data']['published'])
            print("  Views: ", data['data']['views'])

            download_directory = "/sdcard/Download/Tiann-Ai/Youtube Video"
            
            os.makedirs(download_directory, exist_ok=True)

            print("Tunggu Sebentar ...")
            
            response_video = requests.get(video_url, stream=True)
            
            if response_video.status_code == 200:
                video_title = data['data']['title']
                file_name = os.path.join(download_directory, f"{video_title}.mp4")
                file_size = int(response_video.headers.get('content-length', 0))

                progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
                
                with open(file_name, 'wb') as video_file:
                    for chunk in response_video.iter_content(chunk_size=1024):
                        if chunk:
                            video_file.write(chunk)
                            progress_bar.update(len(chunk))

                progress_bar.close()
                print(f"\nVideo downloaded successfully to {file_name}")
            else:
                print(f"Error downloading video: {response_video.status_code}")
                print(response_video.text)
        else:
            print(f"Error getting video information: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
def downau_yt():
    try:
        hu = input("  Masukan URL: ")
        api_url = "https://api.miftahganzz.my.id/api/download/youtube-audio"
        api_key = "skynkt"

        url = f"{api_url}?url={hu}&apikey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            video_url = data['data']['url']
            print("  Judul: ", data['data']['title'])
            print("  Thumbnail: ", data['data']['thumb'])
            print("  Channel: ", data['data']['channel'])
            print("  Published: ", data['data']['published'])
            print("  Views: ", data['data']['views'])

            download_directory = "/sdcard/Download/Tiann-Ai/Youtube Audio"
            
            os.makedirs(download_directory, exist_ok=True)

            print("Tunggu Sebentar ...")
            
            response_video = requests.get(video_url, stream=True)
            
            if response_video.status_code == 200:
                video_title = data['data']['title']
                file_name = os.path.join(download_directory, f"{video_title}.mp4")
                file_size = int(response_video.headers.get('content-length', 0))

                progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
                
                with open(file_name, 'wb') as video_file:
                    for chunk in response_video.iter_content(chunk_size=1024):
                        if chunk:
                            video_file.write(chunk)
                            progress_bar.update(len(chunk))

                progress_bar.close()
                print(f"\nVideo downloaded successfully to {file_name}")
            else:
                print(f"Error downloading video: {response_video.status_code}")
                print(response_video.text)
        else:
            print(f"Error getting video information: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
def down_fb():
    try:
        hu = input("Masukan URL: ")
        api_url = "https://api.miftahganzz.my.id/api/download/facebook"
        api_key = "skynkt"

        url = f"{api_url}?url={hu}&apikey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("  Link Valid!")

            download_choice = input("  Pilih download:\n  1. Video SD\n  2. Video HD\n  3. Audio\nPilihan: ")

            if download_choice == '1':
                download_video(data['data']['video_sd'])
            elif download_choice == '2':
                download_video(data['data']['video_hd'])
            elif download_choice == '3':
                download_audio(data['data']['audio'])
            else:
                print("  Pilihan tidak valid.")
        else:
            print(f"Error getting video information: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
def download_video(video_url):
    try:
        download_directory = "/sdcard/Download/Tiann-Ai/Facebook"
        os.makedirs(download_directory, exist_ok=True)

        file_name = os.path.join(download_directory, f"video_sd.mp4")
        file_size = get_file_size(video_url)

        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)

        with open(file_name, 'wb') as video_file:
            response_video = requests.get(video_url, stream=True)
            for chunk in response_video.iter_content(chunk_size=1024):
                if chunk:
                    video_file.write(chunk)
                    progress_bar.update(len(chunk))

        progress_bar.close()
        print(f"\nVideo downloaded successfully to {file_name}")

    except Exception as e:
        print(f"Error downloading video: {e}")
def download_audio(audio_url):
    try:
        download_directory = "/sdcard/Download/Tiann-Ai/Facebook"
        os.makedirs(download_directory, exist_ok=True)

        file_name = os.path.join(download_directory, f"audio.mp3")
        file_size = get_file_size(audio_url)

        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)

        with open(file_name, 'wb') as audio_file:
            response_audio = requests.get(audio_url, stream=True)
            for chunk in response_audio.iter_content(chunk_size=1024):
                if chunk:
                    audio_file.write(chunk)
                    progress_bar.update(len(chunk))

        progress_bar.close()
        print(f"\nAudio downloaded successfully to {file_name}")

    except Exception as e:
        print(f"Error downloading audio: {e}")
def get_file_size(url):
    response = requests.head(url)
    return int(response.headers.get('content-length', 0))
def gc_wa():
    prompt = input("\nMasukan Query: ")
    url = f"https://api.miftahganzz.my.id/api/search/groupwa?q={prompt}&apikey=skynkt"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for group in data['data']:
            print("Nama: ", group['nama'])
            print("Link: ", group['link'])
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
def bkp_lst():
    url = "https://api.miftahganzz.my.id/api/18/bokep/latest?apikey=skynkt"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for group in data.get('data', []):
            title = group.get('title', 'N/A')
            url = group.get('url', 'N/A')
            views = group.get('views', 'N/A')
            dur = group.get('duration', 'N/A')

            print("Judul: ", title)
            print("Duration: ", dur)
            print("Views: ", views)
            print("Link: ", url,"\n")

    else:
        print(f"Error: {response.status_code}")
        print(response.text)
def vcc():
    print("  AmericanExpress: 349529 | Visa: 464140 | MasterCard: 522146 | Discover: 646809")
    prompt = input("\n  Masukan Bin: ")
    url = f"https://api.lolhuman.xyz/api/vccgenerator?apikey=tianndev&bin={prompt}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for group in data['result']:
            print("Nomor Kartu: ", group['card_number'])
            print("Masa Aktif: ", group['expiration_date'])
            print("CVV: ", group['cvv'])
            print()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

print('''


___________.__                                  _____  .___ 
\__    ___/|__|____    ____   ____             /  _  \ |   |
  |    |   |  \__  \  /    \ /    \   ______  /  /_\  \|   |
  |    |   |  |/ __ \|   |  \   |  \ /_____/ /    |    \   |
  |____|   |__(____  /___|  /___|  /         \____|__  /___|
                   \/     \/     \/                  \/     


''')
print("  1. Chat GPT\n  2. Cek ID Mobile Legends\n  3. Download VIdeo Youtube\n  4. Download Audio Youtube\n  5. Download Video/Audio Facebook\n  6. Download Video Instagram\n  7. Cari Grup Whatsapp\n  8. Bokep Latest\n  9. Random Virtual Credit Card")
hua = input("  Pilih: ")

if hua in ['1']:
        gpt()
if hua in ['2']:
        cek_ml()
if hua in ['3']:
        down_yt()
if hua in ['4']:
        down_yt()
if hua in ['5']:
        down_fb()
if hua in ['6']:
       print("Close")
if hua in ['7']:
        gc_wa()
if hua in ['8']:
        bkp_lst()
if hua in ['9']:
        vcc()
