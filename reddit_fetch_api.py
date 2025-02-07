import praw

# === Configuration ===
# Replace these with your own Reddit app credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
USER_AGENT = 'YOUR_USER_AGENT'  # e.g., 'myRedditApp by /u/yourusername'

SUBREDDIT_NAME = 'python'  # change to your target subreddit
KEYWORD = 'tutorial'       # change to your filter keyword
POST_LIMIT = 50            # number of posts to fetch

# === Initialize the Reddit API client ===
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

subreddit = reddit.subreddit(SUBREDDIT_NAME)

# Fetch the latest posts (using 'new' category)
posts = subreddit.new(limit=POST_LIMIT)

# === Filter posts and collect URLs ===
filtered_urls = []
for post in posts:
    # Check if the keyword exists in the post title (case-insensitive)
    if KEYWORD.lower() in post.title.lower():
        filtered_urls.append(post.url)

# === Store the filtered URLs in a file ===
output_file = "filtered_urls.txt"
with open(output_file, "w") as f:
    for url in filtered_urls:
        f.write(url + "\n")

print(f"Filtered URLs saved to {output_file}")
