# to make a script that will download top 10 youtube meme videos and upload them on my channel
# Step 1 : make function to find top 10 videos
# Step 2 : make a function to download those videos
# Step 3 : make somehow python interact with my youtube account
# Step 4 : upload them in timely manner

#step 1
from googleapiclient.discovery import build



api_key = 'AIzaSyBJZ5dDkov9SvtCzgfJTiy8u_hanJUh5bE'


def top_videos(api_key, max_results=10):
  youtube = build('youtube', 'v3', developerKey=api_key)
  request = youtube.videos().list(
    part ="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",
        maxResults = max_results,
        videoCategoryId="23"
)
  response = request.execute()
  return [item['id'] for item in response['items']]
print(top_videos(api_key))  # Returns list of trending video IDs
