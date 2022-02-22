# Modules for test.py
import requests 
import logging 

# Initialize Logging for Unit Tests
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# Base Address for API
BASE = "http://127.0.0.1:5000/"

# Unit Test #1: Sender ID not present
def test_no_sender_ID():
    logging.info("Running Unit Test #1")
    try:
        # Get a response from the server
        response = requests.get(BASE + "chat/no_sender_ID.json")
        # Format the reponse as a json structure
        arg = response.json()
        # Check the contents of the json structure
        assert arg == {'message':'The sender ID is not present or has an invalid type'}
        logging.info("Unit Test #1 Succeeded")
    # Check the contents of the json structure
    except (AssertionError):
        logging.error("Unit Test #1 Failed")

# Main Function
if __name__ == "__main__":
    test_no_sender_ID()
    logging.info("Ran All Tests")