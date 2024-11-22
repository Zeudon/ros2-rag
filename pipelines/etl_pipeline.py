from clearml import Task, PipelineController
from pymongo import MongoClient
import requests
import youtube_dl

# MongoDB Configuration
MONGO_URI = "mongodb://mongodb:27017/"
DB_NAME = "media_data"
COLLECTION_NAME = "raw_data"

# Connect to MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

# ClearML Task Setup
Task.init(project_name="ETL Pipeline", task_name="Media Ingestion Pipeline")

# Function: Ingest GitHub Documentation
def fetch_github_docs():
    github_urls = [
        "https://github.com/ros2/ros2/releases/download/release-lts/README.md",
        # Add more GitHub URLs for LTS releases here
    ]
    data = []
    for url in github_urls:
        response = requests.get(url)
        if response.status_code == 200:
            collection.insert_one({"source": "GitHub", "url": url, "content": response.text})
            data.append(url)
    return data

# Function: Fetch YouTube Videos Metadata
def fetch_youtube_videos():
    youtube_urls = [
        "https://www.youtube.com/watch?v=example1",
        "https://www.youtube.com/watch?v=example2",
        # Add more YouTube URLs here
    ]
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "writeinfojson": True,
    }
    for url in youtube_urls:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            collection.insert_one({"source": "YouTube", "url": url, "metadata": info})
    return youtube_urls

# Function: Query Ingested URLs
def query_ingested_urls():
    ingested_urls = list(collection.find({}, {"_id": 0, "url": 1}))
    print("Ingested URLs:")
    for entry in ingested_urls:
        print(entry["url"])

# ClearML Pipeline Controller
pipeline = PipelineController(
    project="ETL Pipeline",
    name="ROS2 Media ETL",
    version="1.0"
)

# Add pipeline steps
pipeline.add_function_step(
    name="Fetch GitHub Docs",
    function=fetch_github_docs
)

pipeline.add_function_step(
    name="Fetch YouTube Videos",
    function=fetch_youtube_videos,
    parents=["Fetch GitHub Docs"]
)

pipeline.add_function_step(
    name="Query Ingested URLs",
    function=query_ingested_urls,
    parents=["Fetch YouTube Videos"]
)

# Execute Pipeline
if __name__ == "__main__":
    pipeline.execute()
