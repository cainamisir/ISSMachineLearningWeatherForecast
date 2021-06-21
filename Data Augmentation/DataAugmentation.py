import os
import cv2
from geopy.geocoders import Nominatim
import requests
import json
from exif import Image
import yaml
from geopy import Point
from timezonefinder import TimezoneFinder
from countryinfo import CountryInfo

tf = TimezoneFinder()
geolocator = Nominatim(user_agent="myGeocoder")

def getCityCountry(lat , lon): 
    # Author: Vlad Cainamisir
    # Input:string. format example "lat, lon"; lat & lon are floats
    # Output: a tuple representing the City closest to a group of coordinates

    try:
         location = geolocator.reverse(Point(lat , lon) , language = "en")
    except:
        location = None
    if location != None:
        address = location.raw['address']
        print(address)
        country = address.get('country', '')
        try:
            city = CountryInfo(country).capital()
        except: 
            city = ""
        return city,country
    return "" ,""
    # example query
    # print(getCityCountry("52.509669, 13.376294"))
coords = []

def load_images_from_folder(folder):
    # Author: Vlad Cainamisir
    # Input:string. format: Relative folder location
    # Output: an array of image objects
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            
            imgExif = Image(os.path.join(folder,filename))
            longitude = float(imgExif.gps_longitude[0]) + float(imgExif.gps_longitude[1]) / 60.0 + float(imgExif.gps_longitude[2])/3600.0
            if imgExif.gps_longitude_ref == "W":
                longitude *= -1
            latitude = float(imgExif.gps_latitude[0])+ float(imgExif.gps_latitude[1]) / 60.0 + float(imgExif.gps_latitude[2])/3600.0
            if imgExif.gps_latitude_ref == "S":
                latitude *= -1
            images.append(img)
            
            coords.append(( latitude,longitude ))
    return images
def getWeatherData(city, country):
    # Author: Vlad Cainamisir
    # Input:2 strings. format: city and country
    # Output: outputs the hours when it rains
    response = requests.get("https://www.timeanddate.com/scripts/cityajax.php?n=" + str(country) + "/" + str(city) + "&mode=historic&hd=20210503&month=5&year=2021&json=1") #not really a json
    content = response.content
    start = 0
    end = 0
    opened = 0
    closed = 0
    hourIndex = 0
    skip = 0
    rainCnt = 0
    for i in range(0, len(content)):
        if(start != i - 1 or i == 1):
            if chr(content[i]) == '{':
                opened += 1
            if chr(content[i]) == "}":
                opened -= 1
            if(opened == 0):
                if str(content).find("rain" , start , i) != -1:
                    print("rain at hour" + str(hourIndex))
                    rainCnt += 1
                start = i
                hourIndex += 1
                
    return rainCnt / hourIndex    
    
imgaray = load_images_from_folder("Data/zeus")
imageIndex = 0
dsize = (128, 128)
ind = 0
for img in imgaray:
    directory = ""
    string = str(coords[ind][0]) + ", " + str(coords[ind][1]) 
    try: 
        citycountry = getCityCountry(coords[ind][0] , coords[ind][1])
    except:
        print("oops")
    print(coords[ind][0] , coords[ind][1])
    print(citycountry)
    ind += 1
    if(citycountry[0] != ""):
        rainindex = getWeatherData(citycountry[0] , citycountry[1])
        print(rainindex)
        if rainindex == 0:
            directory = "/clear/"
        elif rainindex > 0 and rainindex < 0.1:
            directory = "/lightrain/"
        elif rainindex > 0.1 and rainindex < 0.5:
            directory = "/mediumrain/"
        elif rainindex > 0.5:
            directory = "/heavyrain/"
        dst = img
        img = cv2.resize(img, (128, 128))
        cv2.imwrite( "Augmentedrun3" + directory + "/photoZeus" + str(imageIndex) + ".jpg", img)
        img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite( "Augmentedrun3" + directory + "/photoZeus90Clockwise" + str(imageIndex) + ".jpg", img_rotate_90_clockwise)
        img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite( "Augmentedrun3" + directory + "/photoZeus90ConterClockwise" + str(imageIndex) + ".jpg", img_rotate_90_counterclockwise)
        img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
        cv2.imwrite( "Augmentedrun3" + directory + "/photoZeus180" + str(imageIndex) + ".jpg", img_rotate_180)
        img_flip_ud = cv2.flip(img, 0)
        cv2.imwrite( "Augmentedrun3" + directory + "/photoZeusFlipVertical" + str(imageIndex) + ".jpg", img_flip_ud)
        img_flip_lr = cv2.flip(img, 1)
        cv2.imwrite( "Augmentedrun3" + directory + "/photoZeusFlipHorizontal" + str(imageIndex) + ".jpg", img_flip_lr)
        img_flip_ud_lr = cv2.flip(img, -1)
        cv2.imwrite( "Augmentedrun3" + directory + "/photoZeusFlipBoth" + str(imageIndex) + ".jpg", img_flip_ud_lr)
        grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite( "Augmentedrun3" + directory + "/GrayscalephotoZeus" + str(imageIndex) + ".jpg", grayScale)
        img_rotate_90_clockwise = cv2.rotate(grayScale, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite( "Augmentedrun3" + directory + "/GrayscalephotoZeus90Clockwise" + str(imageIndex) + ".jpg", img_rotate_90_clockwise)
        img_rotate_90_counterclockwise = cv2.rotate(grayScale, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite( "Augmentedrun3" + directory + "/GrayscalephotoZeus90ConterClockwise" + str(imageIndex) + ".jpg", img_rotate_90_counterclockwise)
        img_rotate_180 = cv2.rotate(grayScale, cv2.ROTATE_180)
        cv2.imwrite( "Augmentedrun3" + directory + "/GrayscalephotoZeus180" + str(imageIndex) + ".jpg", img_rotate_180)
        img_flip_ud = cv2.flip(grayScale, 0)
        cv2.imwrite( "Augmentedrun3" + directory + "/GrayscalephotoZeusFlipVertical" + str(imageIndex) + ".jpg", img_flip_ud)
        img_flip_lr = cv2.flip(grayScale, 1)
        cv2.imwrite( "Augmentedrun3" + directory + "/GrayscalephotoZeusFlipHorizontal" + str(imageIndex) + ".jpg", img_flip_lr)
        img_flip_ud_lr = cv2.flip(grayScale, -1)
        cv2.imwrite( "Augmentedrun3" + directory + "/GrayscalephotoZeusFlipBoth" + str(imageIndex) + ".jpg", img_flip_ud_lr)

        imageIndex = imageIndex + 1

