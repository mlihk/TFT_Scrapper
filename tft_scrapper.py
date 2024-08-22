import praw
import re
import pandas as pd
from collections import defaultdict

reddit = praw.Reddit(client_id='lIkftPNxPIEUWnge7Hg5cQ',
                     client_secret='HJBah6bCX8ZW-pnTyTAXV-xVvduH0w',
                     user_agent='tft_scraper')

#POOL 12 Champions shall be updated each pool
tft_champions = [
    "Ahri", "Akali", "Ashe", "Bard", "Blitzcrank", "Briar", "Camille", "Cassiopeia", 
    "Diana", "Elise", "Ezreal", "Fiora", "Galio", "Gwen", "Hecarim", "Hwei", "Jax", 
    "Jayce", "Jinx", "Kalista", "Karma", "Kassadin", "Katarina", "KogMaw", "Lillia", 
    "Milio", "Mordekaiser", "Morgana", "Nami", "Nasus", "Neeko", "Nilah", "Nomsy", 
    "Norra & Yuumi", "Nunu", "Olaf", "Poppy", "Rakan", "Rumble", "Ryze", "Seraphine", 
    "Shen", "Shyvana", "Smolder", "Soraka", "Swain", "Syndra", "Tahm Kench", "Taric", 
    "Tristana", "Twitch", "Varus", "Veigar", "Vex", "Warwick", "Wukong", "Xerath", 
    "Ziggs", "Zilean", "Zoe"
]

def scrape_tft_subreddit():
    champion_counts = defaultdict(int)

    subreddit = reddit.subreddit('teamfighttactics')
    for post in subreddit.hot(limit=100):
        post_title = post.title.lower()
        post_body = post.selftext.lower()
        
        champions_in_post = set()

        for champion in tft_champions:
            if champion.lower() in post_title or champion.lower() in post_body:
                champions_in_post.add(champion)

        for champion in champions_in_post:
            champion_counts[champion] += 1

    return champion_counts

def save_to_excel(champion_counts):
    df = pd.DataFrame(list(champion_counts.items()), columns=['Champion', 'Count'])
    df.to_excel('tft_champion_counts.xlsx', index=False)
    print("Data saved to tft_champion_counts.xlsx")

champion_counts = scrape_tft_subreddit()

save_to_excel(champion_counts)
