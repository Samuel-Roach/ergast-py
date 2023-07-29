import json
import os
import random
import string

import requests

API_URL = "https://ergast.com/api/f1/status.json?limit=2000"
CURRENT_STATUSES_PATH = "./utils/status-action/current_statuses.json"


def generate_delimiter():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))


def generate_output_string(status_list):
    output = ""
    for status in status_list:
        output += f'- { status["statusId"] } ({ status["status"] })\n'

    return output


def main():
    missing_statuses = []
    response = requests.get(API_URL).json()["MRData"]["StatusTable"]

    with open(CURRENT_STATUSES_PATH, "r") as status_file:
        current = json.loads(status_file.read())

    for status in response["Status"]:
        if status["statusId"] not in current:
            print(
                f'Missing status found: { status["statusId"] } - { status["status"] }'
            )
            missing_statuses.append(status)

    if len(missing_statuses) > 0:
        delim = generate_delimiter() + "\n"
        with open(os.environ["GITHUB_ENV"], "a") as environment_file:
            environment_file.write(f"MISSING_STATUSES_FORMATTED<<{delim}")
            environment_file.write(generate_output_string(missing_statuses))
            environment_file.write(delim)

    with open(os.environ["GITHUB_OUTPUT"], "a") as environment_file:
        environment_file.write(f"MISSING_STATUSES_COUNT={len(missing_statuses)}")


if __name__ == "__main__":
    main()
