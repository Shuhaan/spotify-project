import requests


def extract(url):
    response = requests.get(url)

    return response


if __name__ == "__main__":
    base_url = "https://api.spotify.com"
    endpoint = "v1/albums"

    response = extract(f"{base_url}/{endpoint}")
    print(response.content)
