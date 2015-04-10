import time
import random

access_token = '#'#your access token


from instagram.client import InstagramAPI

api = InstagramAPI(access_token=access_token)

#recent_media, next_ = api.user_recent_media(user_id="sodaglasses", count=10)

def get_media(max_id=0):
    return api.media_search('',100,28.6139,77.2090, max_id=max_id)

def make_for_request_token():
    import datetime
    cur_time = datetime.datetime()
    if cur_time.hour > 2  or cur_time.hour<19:
        wait_time = (19 - cur_time.hour)*3600
    else:
        wait_time = random.randint(5, 60)*60
        yield wait_time
        wait_time + random.randint(40, 60)*60
    return wait_time


def perform_action(media):
    #actions to be performed on media
    api.like_media(media.id)



def main():
    max_id = 0
    medias = []
    for i in range(100):
        medias.extend(get_media(max_id=max_id))
        max_id = medias[-1].id

    for media in medias:
        wait_time = make_for_request_token()
        time.sleep(wait_time)
        perform_action(media)

if __name__ == '__main__':
    main()