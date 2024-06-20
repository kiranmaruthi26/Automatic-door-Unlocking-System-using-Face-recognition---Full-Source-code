from bs4 import BeautifulSoup
import requests
import os
import glob

url = 'https://doorunlocking.getcleared.in/images/'

ext = 'jpg'

images_location = "images/";

def delete_images(images_path):
    images_path = glob.glob(os.path.join(images_path, "*.*"))
    for path in images_path:
        os.remove(path)
        print("Deleted : "+path)
        


def listFD(url, ext=''):
    page = requests.get(url).text
    # print (page)
    soup = BeautifulSoup(page, 'html.parser')
    ls = ['/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return ls


def load_imagesFromServer():
    delete_images(images_location)

    images_path = listFD("https://doorunlocking.getcleared.in/images/", "jpg")

    print("{} images found in server.".format(len(images_path)))

    #print(images_path)

    # Store image encoding and names
    for img_path in images_path:
        img_url = "https://doorunlocking.getcleared.in" + img_path
        print("Image : " + img_path)

        r = requests.get(img_url)
        file_name = img_path[9:]
        print(file_name)
        with open("./images/"+file_name , "wb") as f:
            f.write(r.content)

    print("downloaded images")

#load_imagesFromServer()

