import requests
import random
import string
import time
import os
from discord_webhook import DiscordWebhook 

#Settings:
checkratelimited = "true"
sendwebhookwheninvalid = "true"
sendwebhookwhenratelimited = "true"

#Webhook:
invalidwebhook =  #webhook to be sent jf invalid
validwebhook =  #webhook to be sent when valid

#Debug:
if sendwebhookwhenratelimited == "true":
  if checkratelimited == "false":
    print("You cannot send rate limited webhook when you **check rate limited** setting is false!")
    exit()

#Program
print("Program starting")
while True:
 
   for i in range(1):
    code = "".join(random.choices(
string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))    
     
    url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + 'https://discord.gift/' + code
     
    r = requests.get(url)
    print(r.status_code)
    
    if r.status_code == 200:
      requests.post(validwebhook,json={"content":None, "embeds":[{"title":"Valid nitro founded!","color":200,"fields":[{"name":"Nitro code : ","value":'https://discord.gift/' + code},{"name":"Credit : ","value":"Created by eithan#1349"}]}]}) 
      print("Valid Code Sended | " + 'https://discord.gift/' + code)
    elif r.status_code == 429:
      if checkratelimited == "true":
        print("Rate Limited | " +'https://discord.gift/' + code)
        if sendwebhookwhenratelimited =="true": 
          requests.post(invalidwebhook,json={"content":None, "embeds":[{"title":"Rate Limited Nitro","color":200,"fields":[{"name":"Nitro code : ","value":'https://discord.gift/' + code},{"name":"Credit : ","value":"Created by eithan#1349"}]}]}) 
    elif r.status_code == 404:
      print("Invalid | " + 'https://discord.gift/' + code)
      if sendwebhookwheninvalid == "true":
        requests.post(invalidwebhook,json={"content":None, "embeds":[{"title":"Invalid Nitro","color":200,"fields":[{"name":"Nitro code : ","value":'https://discord.gift/' + code},{"name":"Credit : ","value":"Created by eithan#1349"}]}]}) 
        
        

       


    
    


