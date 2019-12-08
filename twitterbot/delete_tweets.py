from config import create_api
import tweepy

def batch_delete(api):


    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print("Deleted:", status.id)
        except:
            print("Failed to delete:", status.id)


if __name__ == "__main__":
    api = create_api()
    batch_delete(api)