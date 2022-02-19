from numpy import count_nonzero
import requests
import json
url = "https://drand.cloudflare.com/public/latest"
response = requests.get(url)

responses = []
for i in range(response.json()['round']-100,response.json()['round']):
    responses.append(requests.get("https://drand.cloudflare.com/public/"+str(i)).json()["randomness"])
    
responses_bin = []

for response in responses:
    scale = 16
    num_of_bits = 4*len(response)
    responses_bin.append(bin(int(response, scale))[2:].zfill(num_of_bits))

max_ze = 0 
max_one = 0

for responce_bin in responses_bin:
    count_ze = 0
    count_one = 0
    for i in range(len(responce_bin)):
        if responce_bin[i] == '0':
            if count_one > max_one:
                max_one = count_one
            count_one = 0
            count_ze +=1
        else:
            if count_ze >max_ze:
                max_ze = count_ze
            count_ze = 0 
            count_one+=1
            
print("Max zero frequency:",max_ze)
print("Max one frequency:",max_one)