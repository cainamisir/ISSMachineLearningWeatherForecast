import os
import cv2
from geopy.geocoders import Nominatim
import requests
import json
import yaml
geolocator = Nominatim(user_agent="myGeocoder")

def getCityCountry(coords): 
    # Author: Vlad Cainamisir
    # Input:string. format example "lat, lon"; lat & lon are floats
    # Output: a tuple representing the City closest to a group of coordinates

    location = geolocator.reverse(coords , language = "en")
    address = location.raw['address']
    city = address.get('city', '')
    country = address.get('country', '')
    return city,country

    # example query
    # print(getCityCountry("52.509669, 13.376294"))

def load_images_from_folder(folder):
    # Author: Vlad Cainamisir
    # Input:string. format: Relative folder location
    # Output: an array of image objects
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images
def getWeatherData(city, country):
    # Author: Vlad Cainamisir
    # Input:2 strings. format: city and country
    # Output: outputs the hours when it rains
    response = requests.get("https://www.timeanddate.com/scripts/cityajax.php?n=" + str(country) + "/" + str(city) + "&mode=historic&hd=20200428&month=4&year=2020&json=1") #not really a json
    content = response.content
    start = 0
    end = 0
    opened = 0
    closed = 0
    hourIndex = 0
    skip = 0
    for i in range(0, len(content)):
        if(start != i - 1 or i == 1):
            if chr(content[i]) == '{':
                opened += 1
            if chr(content[i]) == "}":
                opened -= 1
            if(opened == 0):
                print("AICI")
                if str(content).find("rain" , start , i) != -1:
                    print("rain at hour" + str(hourIndex))
                start = i
                hourIndex += 1
                print(i)
        
    
#imgaray = load_images_from_folder("Data/zz_bloomers")
imageIndex = 0
dsize = (128, 128)

# for img in imgaray:
#     dst = img

#     img = cv2.resize(img, (128, 128))
#     cv2.imwrite( "Augmented/photo" + str(imageIndex) + ".jpg", img)
#     img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#     cv2.imwrite( "Augmented/photo90Clockwise" + str(imageIndex) + ".jpg", img_rotate_90_clockwise)
#     img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#     cv2.imwrite( "Augmented/photo90ConterClockwise" + str(imageIndex) + ".jpg", img_rotate_90_counterclockwise)
#     img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
#     cv2.imwrite( "Augmented/photo180" + str(imageIndex) + ".jpg", img_rotate_180)
#     img_flip_ud = cv2.flip(img, 0)
#     cv2.imwrite( "Augmented/photoFlipVertical" + str(imageIndex) + ".jpg", img_flip_ud)
#     img_flip_lr = cv2.flip(img, 1)
#     cv2.imwrite( "Augmented/photoFlipHorizontal" + str(imageIndex) + ".jpg", img_flip_lr)
#     img_flip_ud_lr = cv2.flip(img, -1)
#     cv2.imwrite( "Augmented/photoFlipBoth" + str(imageIndex) + ".jpg", img_flip_ud_lr)
#     grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite( "Augmented/Grayscalephoto" + str(imageIndex) + ".jpg", grayScale)
#     img_rotate_90_clockwise = cv2.rotate(grayScale, cv2.ROTATE_90_CLOCKWISE)
#     cv2.imwrite( "Augmented/Grayscalephoto90Clockwise" + str(imageIndex) + ".jpg", img_rotate_90_clockwise)
#     img_rotate_90_counterclockwise = cv2.rotate(grayScale, cv2.ROTATE_90_COUNTERCLOCKWISE)
#     cv2.imwrite( "Augmented/Grayscalephoto90ConterClockwise" + str(imageIndex) + ".jpg", img_rotate_90_counterclockwise)
#     img_rotate_180 = cv2.rotate(grayScale, cv2.ROTATE_180)
#     cv2.imwrite( "Augmented/Grayscalephoto180" + str(imageIndex) + ".jpg", img_rotate_180)
#     img_flip_ud = cv2.flip(grayScale, 0)
#     cv2.imwrite( "Augmented/GrayscalephotoFlipVertical" + str(imageIndex) + ".jpg", img_flip_ud)
#     img_flip_lr = cv2.flip(grayScale, 1)
#     cv2.imwrite( "Augmented/GrayscalephotoFlipHorizontal" + str(imageIndex) + ".jpg", img_flip_lr)
#     img_flip_ud_lr = cv2.flip(grayScale, -1)
#     cv2.imwrite( "Augmented/GrayscalephotoFlipBoth" + str(imageIndex) + ".jpg", img_flip_ud_lr)

#     imageIndex = imageIndex + 1

