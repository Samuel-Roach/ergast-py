import json
import os
import random
import string

import requests

API_URL = "https://ergast.com/api/f1/status.json?limit=2000"
CURRENT_STATUSES_PATH = "./utils/status-action/current_statuses.json"
MISSING_STATUSES = []


def generate_delimiter():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))


def generate_output_string():
    output = ""
    for status in MISSING_STATUSES:
        output += f'- { status["statusId"] } ({status["status"]})\n'

    return output


def main():
    response = requests.get(API_URL).json()["MRData"]["StatusTable"]

    with open(CURRENT_STATUSES_PATH, "r") as status_file:
        current = json.loads(status_file.read())

    if current != response:
        for status in response["Status"]:
            if status not in current:
                MISSING_STATUSES += status

    if len(MISSING_STATUSES) > 0:
        delim = generate_delimiter()
        with open(os.environ["GITHUB_ENV"], "a") as environment_file:
            environment_file.write(f"MISSING_STATUSES<<{delim}")
            environment_file.write(generate_output_string())
            environment_file.write(delim)

    with open(os.environ["GITHUB_OUTPUT"], "a") as environment_file:
        environment_file.write(f"MISSING_STATUSES_COUNT={len(MISSING_STATUSES)}")


if __name__ == "__main__":
    main()
