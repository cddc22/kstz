import requests
import base64
import os
import argparse
import getpass

def upload_to_gist(content, gist_id, github_token, filename):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        "files": {
            filename: {
                "content": content
            }
        }
    }
    try:
        response = requests.patch(url, headers=headers, json=data)
        response.raise_for_status()
        print(f"Successfully updated Gist: {gist_id}")
    except requests.RequestException as e:
        print(f"Error updating Gist: {e}")

def main():
    parser = argparse.ArgumentParser(description='Process GitHub Token.')
    parser.add_argument('github_token', type=str, help='Your GitHub Token')
    args = parser.parse_args()

    # Encrypt the GitHub token and convert it to base64
    github_token = base64.b64encode(args.github_token.encode()).decode()

    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, 'data', 'clash.yaml')

    with open(file_path, 'r') as file:
        content = file.read()

    # Upload the content to the Gist
    gist_id = '712fc9f08cd794ca28352f7df2745cd5'
    filename = 'clash.yaml'  # Specify the desired filename
    upload_to_gist(content, gist_id, github_token, filename)

if __name__ == "__main__":
    main()
