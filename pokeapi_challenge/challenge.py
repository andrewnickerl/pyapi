#! python3

import requests
import wget

def api_pull():
    choice = input("What Pokemon would you like a picture of? ").lower()
    pokedict = requests.get(f"https://pokeapi.co/api/v2/pokemon/{choice}").json()
    return pokedict

def api_slice(json2python):
    poke_pic = json2python['sprites']['front_default']
    return poke_pic

def wget_pic(imagelink):
    wget.download(imagelink, r'C:\Users\Andrew\OneDrive\Desktop')

def main():
    wget_pic(api_slice(api_pull()))

if __name__ == '__main__':
    main()