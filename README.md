
# YouTube Data Scraper

This Python project fetches and processes data for the top 500 YouTube videos of a given genre. The script utilizes the YouTube Data API to gather detailed information about the videos and saves the results into a CSV file.

## Features

- Dynamically searches for videos based on a user-specified genre.
- Fetches detailed metadata for each video, including:
  - Video URL
  - Title
  - Description
  - Channel Title
  - Keyword Tags
  - Category
  - Topic Details
  - Published Date
  - Video Duration
  - View Count
  - Comment Count
  - Captions Availability
  - Location of Recording
- Outputs the data in a clean, structured CSV file.

## Requirements

- Python 3.7+
- A valid YouTube Data API key.

## Setup

1. Clone the repository or download the script file.
2. Install the required Python libraries using:
   ```bash
   pip install google-api-python-client pandas python-dotenv
   ```
3. Create a `.env` file in the project directory and add your YouTube Data API key:
   ```env
   YOUTUBE_API_KEY=your_api_key_here
   ```

## Usage

1. Run the script:
   ```bash
   python your_script_name.py
   ```
2. Enter a genre (e.g., "music", "comedy") when prompted.
3. The script will:
   - Search for the top 500 videos in the specified genre.
   - Fetch detailed metadata for the videos.
   - Save the processed data in a CSV file named `youtube_data.csv`.

## Output

The output CSV file contains the following columns:
- **Video URL**: Direct link to the video.
- **Title**: Video title.
- **Description**: Video description.
- **Channel Title**: Name of the channel.
- **Keyword Tags**: Tags associated with the video.
- **Category**: Video category ID.
- **Topic Details**: Topics associated with the video.
- **Published Date**: Date when the video was published.
- **Video Duration**: Duration of the video.
- **View Count**: Number of views.
- **Comment Count**: Number of comments.
- **Captions Availability**: Whether captions are available (true/false).
- **Captions Text**: Placeholder for captions text.
- **Location of Recording**: Video's recording location, if available.

## Limitations

- The script does not fetch caption text due to API constraints.
- API quotas may limit the number of requests that can be made daily.
- The script assumes that all videos have metadata available, which may not always be true.

## Future Enhancements

- Add functionality to fetch and save caption text for videos with captions.
- Implement error handling for videos with incomplete metadata.
- Optimize API usage to handle larger datasets efficiently.

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- [Google YouTube Data API](https://developers.google.com/youtube/registering_an_application)
- Python libraries: `google-api-python-client`, `pandas`, `dotenv`.

---
