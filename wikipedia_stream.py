from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
import json
import time

# Step 1: Configure PubNub
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-83a959c1-2a4f-481b-8eb0-eab514c06ebf"  # PubNub Subscribe Key
pnconfig.ssl = True 
pnconfig.uuid = 'MyIdentifier'  
pubnub = PubNub(pnconfig)


# Step 2: Initialize global variables
change_count = 0
changes_list = []


# Step 3: Calculate time and change difference.
class WikipediaChangeListener(SubscribeCallback):
    def __init__(self, start_time, duration):
        super().__init__()
        self.start_time = start_time
        self.duration = duration

    def message(self, pubnub, message):
        global change_count, changes_list

        # Check if the time limit has been reached
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.duration:
            print("\nTime limit reached. Stopping the stream...")
            pubnub.unsubscribe_all()
            return

        # Increment the change count and store the message
        change_count += 1
        changes_list.append(message.message)

        # Print the current count and details of the change
        print(f"Change #{change_count}: {message.message}")

        # Periodically save the data to a JSON file
        if change_count % 10 == 0:  # Save every 10 changes
            with open("wikipedia_changes.json", "w") as file:
                json.dump(changes_list, file, indent=4)


# Step 3: Main execution
def main():
    global change_count, changes_list

    # Start the timer and set the duration (10 minutes = 600 seconds)
    start_time = time.time()
    duration = 600  # 10 minutes in seconds

    listener = WikipediaChangeListener(start_time, duration)
    pubnub.add_listener(listener)

    try:
        print("Starting to listen to the Wikipedia data stream...")
        pubnub.subscribe().channels("pubnub-wikipedia").execute()

        # Keep the script running until the time limit is reached
        while time.time() - start_time < duration:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped listening to the data stream manually.")
    finally:
        # Save all remaining data to the JSON file
        with open("wikipedia_changes.json", "w") as file:
            json.dump(changes_list, file, indent=4)
        print("All changes saved to 'wikipedia_changes.json'.")

if __name__ == "__main__":
    main()