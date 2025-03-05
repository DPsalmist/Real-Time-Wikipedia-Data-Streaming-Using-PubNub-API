# Real-Time-Wikipedia-Data-Streaming-Using-PubNub-API

*Title:* Real-Time Wikipedia Data Streaming Using PubNub API

*Objective:* To capture and process real-time edit events from Wikipedia using PubNub's data streaming capabilities.

*Features:*

- **PubNub Integration:** Utilizes PubNub's subscribe key to access the live stream of Wikipedia edits.
- **Real-Time Data Handling:** Implements a listener to process incoming data streams and store them for analysis.
- **Time-Bound Streaming:** Data collection with automated saving at regular intervals e.g., 10 minutes.
- **JSON Storage:** Processing and storage of received events into a JSON file.


*Prerequisites:*

Python 3.x installed.
Required Python packages: pubnub, json, time.

*Setup Instructions:*

1. **Clone the Repository**
    - git clone https://github.com/yourusername/pubnub-wikipedia-streaming.git
    - cd pubnub-wikipedia-streaming

2. **Install Dependencies**
   - pip install -r requirements.txt

3. **Run app**
   - python wikipedia_stream.py

*Usage:*
- The script subscribes to PubNub's Wikipedia channel and listens for live edit events.
- Received events are printed to the console and saved into wikipedia_changes.json.
- The script runs for a predefined duration (e.g., 10 minutes) and saves data at regular intervals (e.g., every 10 changes).

*References:*
   - Links to PubNub documentation and related resources. PubNub Python SDK
   - https://www.pubnub.com/demos/real-time-data-streaming/
