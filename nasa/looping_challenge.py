#! python3

import requests


def main():
    apodresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()

    cam = input("Which camera from Curiosity would you like to see pictures from? Options are:  FHAZ, RHAZ, MAST, CHEMCAM, NAVCAM\n")

    while cam != 'FHAZ' and cam != 'RHAZ' and cam != 'MAST' and cam != 'CHEMCAM' and cam != 'NAVCAM':
        cam = input("Invalid option. Options are:  FHAZ, RHAZ, MAST, CHEMCAM, NAVCAM\n")

    for photo in apodresp['photos']:
        if photo['camera']['name'] == cam:
            print("ROVER: " + photo['rover']['name'])
            print("DATE: " + photo['earth_date'])
            print("SOURCE URL: " + photo['img_src'] + "\n")

if __name__ == "__main__":
    main()