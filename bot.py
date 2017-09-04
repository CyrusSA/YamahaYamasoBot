import praw
import config
import time

def bot_login():
    r=praw.Reddit(username = config.username,
                  password = config.password,
                  client_id = config.client_id,
                  client_secret = config.client_secret,
                  user_agent = 'Yamaha Yamaso Bot')
    print('Logged in')
    
    return r

def run_bot(r):
    print('Retrieving Comments')
    for comment in r.subreddit('guitar').stream.comments():
        flag=0
        with open('don_reply.txt', 'r') as f:
            list_comments = f.read().split('\n')
            if 'yamaha' in comment.body.lower() and comment.author != r.user.me() and comment.id not in list_comments:
                print('Commenting')
                comment.reply('''>Yamaha

[Yamaso](https://www.youtube.com/watch?v=CsILdk9Mrug)''')
                l=comment.id
                flag=1

                print('Sleeping')
                time.sleep(600)
                print('Sleep Over')
        if flag ==1:
            with open('don_reply.txt', 'a') as f:
                f.write(l + '\n')
            
        
r = bot_login()
run_bot(r)
