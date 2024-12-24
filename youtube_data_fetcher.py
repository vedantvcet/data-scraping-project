import os
import csv
import time
from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Initialize YouTube API client
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)


def search_videos(query, max_results=500):
    """Search for videos by genre."""
    results = []
    next_page_token = None
    while len(results) < max_results:
        try:
            response = youtube.search().list(
                q=query,
                part="id,snippet",
                type="video",
                maxResults=min(50, max_results - len(results)),
                pageToken=next_page_token,
            ).execute()
            results.extend(response.get("items", []))
            next_page_token = response.get("nextPageToken")
            if not next_page_token:
                break
        except Exception as e:
            print(f"Error during search: {e}")
            break
        time.sleep(1)  # Handle API rate limits
    return results


def fetch_video_details(video_ids):
    """Fetch detailed information for a list of video IDs."""
    details = []
    for i in range(0, len(video_ids), 50):
        try:
            response = youtube.videos().list(
                part="snippet,statistics,contentDetails,topicDetails,recordingDetails",
                id=",".join(video_ids[i:i + 50]),
            ).execute()
            details.extend(response.get("items", []))
        except Exception as e:
            print(f"Error fetching video details: {e}")
            break
        time.sleep(1)
    return details


def process_video_data(videos):
    """Extract required fields from video data."""
    processed_data = []
    for video in videos:
        snippet = video.get("snippet", {})
        statistics = video.get("statistics", {})
        content_details = video.get("contentDetails", {})
        recording_details = video.get("recordingDetails", {})
        topic_details = video.get("topicDetails", {})

        processed_data.append({
            "Video URL": f"https://www.youtube.com/watch?v={video.get('id')}",
            "Title": snippet.get("title"),
            "Description": snippet.get("description"),
            "Channel Title": snippet.get("channelTitle"),
            "Keyword Tags": ", ".join(snippet.get("tags", [])),
            "Category": snippet.get("categoryId"),
            "Topic Details": ", ".join(topic_details.get("topicCategories", [])),
            "Published Date": snippet.get("publishedAt"),
            "Video Duration": content_details.get("duration"),
            "View Count": statistics.get("viewCount"),
            "Comment Count": statistics.get("commentCount"),
            "Captions Availability": "caption" in content_details.get("caption", ""),
            "Captions Text": "Not Fetched",  # Placeholder
            "Location of Recording": recording_details.get("location"),
        })
    return processed_data


def save_to_csv(data, filename="youtube_data.csv"):
    """Save processed data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"Data saved to {filename}")


def main():
    genre = input("Enter a genre: ")
    print("Searching videos...")
    search_results = search_videos(genre)
    video_ids = [item["id"]["videoId"] for item in search_results if "id" in item]

    print("Fetching video details...")
    video_details = fetch_video_details(video_ids)

    print("Processing video data...")
    processed_data = process_video_data(video_details)

    print("Saving data to CSV...")
    save_to_csv(processed_data)
    print("Task completed!")


if __name__ == "__main__":
    main()
