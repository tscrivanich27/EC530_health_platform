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
    # Catch Assertion Error
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
        logging.info("Unit Test #2 Succeeded")
    # Catch Assertion Error
    except (AssertionError):
        logging.error("Unit Test #2 Failed")

# Unit Test #3: Device Serial Number is not present
def test_no_device_serial_number():
    logging.info("Running Unit Test #3")
    try:
        # Get a response from the server 
        response = requests.get(BASE + "devices/no_device_serial_number.json")
        # Format the response as a json structure
        arg = response.json()
        # Check the contents of the json structure
        assert arg == {'message': 
            'The serial number is not present or has an invalid type'}
        logging.info("Unit Test #3 Succeeded")
    # Catch Assertion Error
    except (AssertionError):
        logging.error("Unit Test #3 Failed")

# Unit Test #4: Device Serial Number has an invalid type
def test_invalid_serial_number_type():
    logging.info("Running Unit Test #4")
    try:
        # Get a response from the server
        response = requests.get(BASE + "devices/wrong_device_serial_number_type.json")
        # Format the response as a json structure
        arg = response.json()
        # Check the contents of the json structure
        assert arg == {'message':
            'The serial number is not present or has an invalid type'}
        logging.info("Unit Test #4 Succeeded")
    # Catch Assertion Error
    except (AssertionError):
        logging.error("Unit Test #4 Failed")

# Unit Test #5: Device Data not present
def test_no_device_data():
    logging.info("Running Unit Test #5")
    try:
        # Get a response from the server
        response = requests.get(BASE + "devices/no_device_data.json")
        # Format the response as a json structure
        arg = response.json()
        # Check the contents of the json structure
        assert arg == {'message':
            'The data is not present or has an invalid type'}
        logging.info("Unit Test #5 Succeeded")
    # Catch Assertion Error
    except (AssertionError):
        logging.error("Unit Test #5 Failed")
        
# Unit Test #6: Device Data has invalid type
def test_invalid_data_type():
    logging.info("Running Unit Test #6")
    try:
        # Get a response from the server
        response = requests.get(BASE + "devices/wrong_device_data_type.json")
        # Format the response as a json structure
        arg = response.json()
        # Check the contents of the json structure
        assert arg == {'message':
            'The data is not present or has an invalid type'}
        logging.info("Unit Test #6 Succeeded")
    # Catch Assertion Error
    except (AssertionError):
        logging.error("Unit Test #6 Failed")

def test_no_sender_id():
    logging.info("Running Unit Test #7")
    try:
        response = requests.get(BASE + "chat/no_sender_id.json")
        arg = response.json()
        assert arg == {'message':
            'The sender ID is not present or has an invalid type'}
        logging.info("Unit Test #7 Succeeded")
    except (AssertionError):
        logging.error("Unit Test #7 Failed")

def test_no_sender():
    logging.info("Running Unit Test #8")
    try:
        response = requests.get(BASE + "chat/no_sender.json")
        arg = response.json()
        assert arg == {'message':
            'The user sender is not present or has an invalid type'}
        logging.info("Unit Test #8 Succeeded")
    except (AssertionError):
        logging.error("Unit Test #8 Failed")

# Function to send data to MongoDB 
def test_db():
    logging.info("Running First Database Test")
    # Get request for first valid json entry
    requests.get(BASE + "devices/valid_entry.json")
    # Get request for second valid json entry
    requests.get(BASE + "devices/valid_entry_second.json")
    # Get request for third valid json entry
    requests.get(BASE + "chat/valid_entry_third.json")
    logging.info("Ran First Database Test")

# Main function 
if __name__ == "__main__":
    test_no_device_id()
    test_invalid_id_type()
    test_no_device_serial_number()
    test_invalid_serial_number_type()
    test_no_device_data()
    test_invalid_data_type()
    test_no_sender_id()
    test_no_sender()
    test_db()
    logging.info("Ran All Tests")