#!/usr/bin/python3

import http.client
import json
from time import sleep

config = dict()

def read_config():
    with open("config.conf", "r") as file:
        content = file.read().split("\n")
        for i in content:
            if len(i) > 0 and i[0] != '#':
                key, value = i.split("=")
                config[key] = value

def get_github_headers():
    headers = {
        "User-Agent": config['GITHUB_USER'],
        "Authorization": "Token " + config['GITHUB_AUTH_TOKEN']
    }
    
    return headers

def get_last_hash():
    file = open("lasthash.dat", "r+")
    data = file.read()
    file.close()
    return data

def write_last_hash(hash):
    file = open("lasthash.dat", "w+")
    file.write(hash)
    file.close()

def get_current_hash():
    con = http.client.HTTPSConnection(config['GITHUB_API'])
    con.request("GET", "/repos/" + config['GITHUB_REPO_OWNER'] + "/" + config['GITHUB_REPO_NAME'] + "/git/refs/heads/" + config['GITHUB_REPO_BRANCH'], None, get_github_headers())
    response = con.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    con.close()
    
    return data['object']['sha']

def trigger_rebuild():
    headers = {
        "Authorization": "Token " + config['OBS_TOKEN'],
        "project": config['OBS_PROJECT'],
        "package": config['OBS_PACKAGE']
    }
    
    con = http.client.HTTPSConnection(config['OBS_API'])
    con.request("POST", "/trigger/runservice", None, headers)
    response = con.getresponse()
    data = response.read()

if __name__ == '__main__':
    lasthash = ""
    currhash = ""
    
    read_config()
    
    while True:
        lasthash = get_last_hash()
        currhash = get_current_hash()
        
        if currhash != lasthash:
            lasthash = currhash
            write_last_hash(currhash)
            
            print("New commit detected - I'll trigger a rebuild now: " + lasthash)
            trigger_rebuild()
        
        sleep(5)