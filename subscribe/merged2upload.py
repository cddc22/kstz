import requests
import os
import argparse

# 异或加密函数
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# 上传到 Gist 的函数
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

    # 定义密钥
    key = 0x55  # 这是一个示例密钥，你可以使用任何整数作为密钥

    # 对 GitHub 令牌进行异或加密
    github_token_encrypted = xor_encrypt_decrypt(args.github_token, key)

    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, 'data', 'clash.yaml')

    with open(file_path, 'r') as file:
        content = file.read()

    # 上传内容到 Gist
    gist_id = '712fc9f08cd794ca28352f7df2745cd5'
    filename = 'clash.yaml'  # 指定所需的文件名
    # 在上传之前，需要将令牌解密
    github_token_decrypted = xor_encrypt_decrypt(github_token_encrypted, key)
    upload_to_gist(content, gist_id, github_token_decrypted, filename)

if __name__ == "__main__":
    main()
