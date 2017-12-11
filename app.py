import os

from flask import Flask, request, render_template, send_from_directory
import mechanize
import re

import time
# from lxml import html  
# import xlwt 
# import xlrd 
from django.utils.http import urlquote 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome('C:\Users\Dev\Downloads\chromedriver_win32\chromedriver.exe') 
#change location here, download chrome driver
driver.maximize_window()
def search_amazon(search_string):
    static_search_amazon = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='
    driver.get(static_search_amazon+urlquote(search_string).encode('utf8'))

def search_walmart(search_string):
    static_search_walmart1 = 'https://www.walmart.com/search/?query='
    static_search_walmart2 = '&cat_id=0'
    driver.get(static_search_walmart1+urlquote(search_string).encode('utf8')+static_search_walmart2)

@app.route("/")
def index():
    return render_template("upload.html")

def object_recognizer():
    f = open("temp.txt","w+")
    f.write("Line 1 \n")
    f.write("Line 2 \n")
    f.close();
    delete_line()
def delete_line():
    f = open("temp.txt","r+")
    lines = f.readlines()
    f.seek(0)
    #get the line you want no need to delete line
    # for line in lines:
    #     if some condition:
    #         get line
    #search websites for the product
    search_amazon(line)
    search_walmart(line)


@app.route("/complete", methods=["POST"])
def detect_function():
    #call object recognzer here
    file = object_recognizer()
    print "doneee"

@app.route("/foobar", methods=["POST"])
def foobar():
    print "inside foobar"

@app.route("/upload", methods=["POST"])
def upload():
   # folder_name = request.form['superhero']
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    target = os.path.join(APP_ROOT, 'static')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported
        # ext = os.path.splitext(filename)[1]
        # if (ext == ".jpg") or (ext == ".png"):
            # print("File supported moving on...")
        # else:
            # render_template("Error.html", message="Files uploaded are not supported...")
        destination = "/".join([target, "temp.jpg"])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("complete.html", image_name=filename)
    #print "heyho"
    return render_template("complete.html")


# @app.route('/upload/<filename>')
# def send_image(filename):
#     return send_from_directory("images", filename)


# @app.route('/gallery')
# def get_gallery():
#     image_names = os.listdir('./images')
#     print(image_names)
#     return render_template("gallery.html", image_names=image_names)


if __name__ == "__main__":
    app.run(port=4555, debug=True)
