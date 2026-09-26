import json
import time


def load_test_data():

    with open("test_data/test_data.json", "r") as file:
        return json.load(file)


def generate_unique_email():

    return f"monalisa{int(time.time())}@example.com"