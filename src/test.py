import requests
#
#
# user = "skypro-008"
# url = f"https://api.github.com/users/{user}/repos"
#
# response = requests.get(url)
#
# repos = response.json()
#
# for repo in repos:
#     if repo['language'] == "Python":
#         print(f"Name: {repo['name']}\nLink: {repo['html_url']}\n")
#

url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=EUR&amount=1200"
headers = {
    "apikey": "fSHSoKuZ2zVFxstaVw1stEq3GIFqPptc"
}

it = requests.get(url, headers=headers)

status_code = it.status_code
result = it.json()

print(status_code)
print(result)
