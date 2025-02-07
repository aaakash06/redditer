import requests
from bs4 import BeautifulSoup

# === Configuration ===
SUBREDDIT_NAME = 'forhire'  # change to your target subreddit
KEYWORD = '[hiring]'       # change to your filter keyword
URL = f"https://old.reddit.com/r/{SUBREDDIT_NAME}/new/"

# Use a valid User-Agent header to avoid being blocked
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36"
}

# === Fetch the webpage ===
response = requests.get(URL, headers=headers)
if response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
    exit()

# === Parse the page with BeautifulSoup ===
soup = BeautifulSoup(response.content, "html.parser")
# In old.reddit.com each post is inside a <div> with class "thing"
posts = soup.find_all("div", class_="thing")

# === Filter posts and collect URLs ===
filtered_urls = []
for post in posts:
    title_element = post.find("a", class_="title")
    if title_element and KEYWORD.lower() in title_element.text.lower():
        # Get the post permalink and form a complete URL
        permalink = post.get("data-permalink")
        if permalink:
            full_url = "https://old.reddit.com" + permalink
            filtered_urls.append(full_url)

# === Store the filtered URLs in a file ===
output_file = "filtered_urls.txt"
with open(output_file, "w") as f:
    for url in filtered_urls:
        f.write(url + "\n")

print(f"Filtered URLs saved to {output_file}")
