# Modules for test.py
import requests 
import logging

# Initialize Logging for Unit Tests
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# Base Address for API
BASE = "http://127.0.0.1:5000/"

# Unit Test #1: Device ID is not present
def test_no_device_id():
    logging.info("Running Unit Test #1")
    try:
        # Get a response from the server 
        response = requests.get(BASE + "devices/no_device_id.json")
        # Format the reponse as a json structure
        arg = response.json()
        # Check the contents of the json structure
        assert arg == {'message': 
            'The device ID is not present or has an invalid type'}
        logging.info("Unit Test #1 Succeeded")
    # Catch Assertation Error
    except (AssertionError):
        logging.error("Unit Test #1 Failed")

# Unit Test #2: Device ID has an invalid type
def test_invalid_id_type():
    logging.info("Running Unit Test #2")
    try:
        # Get a response from the server
        response = requests.get(BASE + "devices/wrong_device_id_type.json")
        # Format the response as a json structure
        arg = response.json()
        # Check the contents of the json structure
        assert arg == {'message': 
            'The device ID is not present or has an invalid type'}
        logging.info("Unit Test #2 Succeesed")
    # Catch Assertation Error
    except (AssertionError):
        logging.error("Unit Test #2 Failed")

# Main function 
if __name__ == "__main__":
    test_no_device_id()
    test_invalid_id_type()
    logging.info("Ran All Tests")