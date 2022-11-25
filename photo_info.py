import requests, json
import configparser
import time
from tqdm import tqdm
import yadisk

config = configparser.ConfigParser()
config.read('settings.ini')

class VK:

    def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

    def get_photo_vk(self):
        count = 1
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': self.id,
            'access_token': self.token,
            'v' : self.version,
            'album_id' : 'wall',      
            'extended' : 1,
            'photo_sizes': True
            }
        response = requests.get(url, params)
        response.raise_for_status()
        result = response.json()
       
        dict_result = dict.fromkeys(['file_name', 'size'])
        for file in tqdm(result['response']['items']):
            time.sleep(1)
            self.size = file['sizes'][-5]['type']
            photo_url = file['sizes'][-1]['url']
            file_name = file['likes']['count']
            file_name1 = file_name + count
            download_photo = requests.get(photo_url)

            with open(f'{file_name1}.jpg', 'wb') as f:
                f.write(download_photo.content)
                
            dict_result['file_name'] = file_name1
            dict_result['size'] = self.size
            print(dict_result)

            with open('result.json', 'w') as file:
                json.dump(dict_result, file, indent=2, ensure_ascii=False)

            count += 1
        return response.json() 
   
def write_json(data):
    with open('response.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

class YA:
    
    def __init__(self, ya_token):
       self.token = ya_token

    def add_folder(self):
        y = yadisk.YaDisk(token = self.token)
        print(y.check_token())
        y.mkdir("/photo_vk")
        for photo in range(1, 6):
            y.upload(f'{photo}.jpg', f'/photo_vk/{photo}.jpg')


if __name__ == '__main__':

    access_token = ''
    user_id = 431223329
    vk = VK(access_token, user_id)

    ya_token = ''
    ya = YA(ya_token)

    print(vk.get_photo_vk())
    write_json(vk.get_photo_vk())
    ya.add_folder()