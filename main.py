from webserver import keep_alive
import requests

channelID = 1010487038165925938
headers = {
    "authorization":
    "MTAwNzY5Njk1ODMxMzQ4NDM3OQ.GAXAfx.4RVdW9KKbGniWzmEMJsBkBWaYBWtKWxRCrmTwA"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
