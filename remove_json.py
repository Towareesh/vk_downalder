import time
import json

import vk_api
from vk_api import audio


class UserLoginVk:
    def __init__(self, login, password, userid=None, token=None):
        self.login      = login
        self.password   = password
        self.userid     = userid

        self.vk_session = vk_api.VkApi(login=login,
                                       password=password,
                                       auth_handler=self._sms_confirmation,
                                       token=token)
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()


    def _sms_confirmation(self):
        key = input('Enter sms code: ')
        remember_me = True
        return key, remember_me


    def _get_audio(self):
        vk_audio = audio.VkAudio(self.vk_session)
        return vk_audio


    def get_json_audio(self):
        list_audio = self._get_audio()
        with open('my_tracks2.json', 'w') as file:
            json.dump(list_audio.get(owner_id=self.userid), file, indent=2)


    def my_albums(self):
        albums = self._get_audio()
        with open('my_albums.json', 'w') as file:
            json.dump(albums.get_albums(owner_id=self.userid), file, indent=2)


def main_script(login, password, userid):
    my_vk = UserLoginVk(login, password, userid)
    my_vk.my_albums()

def register():
    userid = input('If have id: ')
    if not userid:
        userid = None

    login    = input('Enter login or phone: ')
    password = input('Enter password: ')

    try:
        main_script(login, password, userid)
    except vk_api.exceptions.Captcha as captcha:
        captcha.sid             # Получение sid
        captcha.get_url()       # Получить ссылку на изображение капчи
        captcha.get_image()     # Получить изображение капчи (jpg)
        main_script(login, password, userid)

if __name__ == '__main__':
    start_time = time.time()
    register()
    end_time = time.time() - start_time
    print(round(end_time, 2))
