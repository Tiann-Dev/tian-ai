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
        hu = input("Masukan URL: ")
        api_url = "https://api.miftahganzz.my.id/api/download/youtube-video"
        api_key = "skynkt"

        url = f"{api_url}?url={hu}&apikey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            video_url = data['data']['url']
            print("Judul: ", data['data']['title'])
            print("Thumbnail: ", data['data']['thumb'])
            print("Channel: ", data['data']['channel'])
            print("Published: ", data['data']['published'])
            print("Views: ", data['data']['views'])

            download_directory = "/sdcard/Download/Tiann-Ai/Video"
            
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



print('''


AI TIAN


''')
print("1. Chat GPT\n2. Cek ID Mobile Legends\n3. Download VIdeo Youtube")
hua = input("Pilih: ")

if hua in ['1']:
        gpt()
if hua in ['2']:
        cek_ml()
if hua in ['3']:
        os.system("mkdir video")
        down_yt()
