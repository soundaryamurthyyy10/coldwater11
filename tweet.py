import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "7Oqvowt4rcmbaLMYimVcGXBod",	
    "consumer_secret"     : "YOASU2Eu5dQsC9DKk1pdC6XVzTLJNXTcFmb6G7CgKWpyrZuhvy",
    "access_token"        : "971949971598536704-u5pL0eq6SikZixDJVsQKoP0bmXWzCLV",
    "access_token_secret" : "4GL1wyO6lnkamKxrqavsWsF1KvjqVKnk4x1UY67CC59An"
    }
  api = get_api(cfg)
  tweet = "Hello, world!...."
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
