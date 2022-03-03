import requests, config.credentials as credentials

def send(data):
    groupID = credentials.groupID
    # Send the response to the group
    post_params = { 'bot_id' : credentials.botID, 'text': data } 
    requests.post('https://api.groupme.com/v3/bots/post', params = post_params)

#send("test")