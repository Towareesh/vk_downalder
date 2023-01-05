import json
import time
import os
import subprocess


def view_audio(json_data, stop):
    n = 0
    for track_data in json_data:
        n += 1
        track_name     = '{} - {}.mp3'.format(track_data['artist'], track_data['title'])
        lisnk_segments = track_data['url']
        print(f'{n}>> {track_name}')

        # subprocess.call(f"""ffmpeg -i {lisnk_segments} {n}.mp3""", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(f"""ffmpeg -i {lisnk_segments} {n}.mp3""")
        os.rename(f'{n}.mp3', track_name)

        if n == stop:
            break
        


with open('my_tracks2.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)


start_time = time.time()

view_audio(data, 2)
end_time = time.time() - start_time
print(round(end_time, 2))