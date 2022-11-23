import requests

class VK:

    def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

    def get_photo_vk(self, offset = 0, count = 5):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': self.id,
            'access_token': self.token,
            'v' : self.version,
            'album_id' : 'wall',      
            'extended' : 1,
            'photo_sizes': 1,
            #'offset' : offset,
            #'count' : count
            }
        response = requests.get(url, params)
        return response.json()

    #def parsed_photo(self, photos_info)


access_token = 'vk1.a.7xInOKYWj1M2HM68kQ3FiCeOZY_FhdJrma4MRbTje_jWY80eTnrIcB_fAYC_UyX1KyPoPFn8FNk6R_ZOAJPkqmgXYZ5F1tb_nM2eI2z-d1O7KxZUzIufhpt_U2_TM6270TlTw7_Ugjs4EiO4rpgMmrDas6Ef5CIvIoXVlI0QGP06yVV2mnEtb2JE-KxxaFKt5bUkoctCed_dFSf6YTe6gA'
user_id = 431223329
vk = VK(access_token, user_id)
print(vk.get_photo_vk())
