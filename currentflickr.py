#!/usr/bin/python

from flickrapi import FlickrAPI, shorturl
from appscript import app, its, k
import re

def currentFlickrID():
  '''Return the ID for the Flickr image currently showing in the browser.
  
  The function works through Apple Events and supports only the Safari and
  Chrome browsers. It will generate an IndexError if the frontmost tab of
  the browser isn't showing a Flickr image.'''
  
  # The regex for extracting user and photo info.
  infoRE = r'flickr\.com/photos/(.*)/(\d+)/?'

  # Get the URL of the current page in either Safari or Chrome.
  numSafari = app('System Events').processes[its.name == 'Safari'].count(each=k.item)
  numChrome = app('System Events').processes[its.name == 'Google Chrome'].count(each=k.item)

  if numSafari > 0:
    thisURL = app('Safari').documents[0].URL.get()
  elif numChrome > 0:
    frontIndex = app('Google Chrome').windows[1].active_tab_index.get()
    thisURL = app('Google Chrome').windows[1].tabs[frontIndex].URL.get()

  # Extract the user and photo info from the URL.
  info = re.findall(infoRE, thisURL)
  return info[0][1]
  
def currentFlickrTitle():
  '''Return the title of the Flickr image currently showing in the browser.

  The function works through Apple Events and supports only the Safari and
  Chrome browsers.'''

  # Flickr parameters
  fuser = 'Flickr username'
  key = 'Get key from Flickr'
  secret = 'Get secret from Flickr'

  # Get the image ID.
  try:
    imageID = currentFlickrID()
  except IndexError:
    return "Not a Flickr image"

  # Establish the connection with Flickr.
  flickr = FlickrAPI(api_key=key, secret=secret)

  # Get the title.
  etree = flickr.photos_getInfo(photo_id = imageID, format = 'etree')
  for i in etree[0]:
   if i.tag == 'title':
     return i.text
     break

  # If the size wasn't found.
  return "Title not found"


def currentFlickrURL(kind):
  '''Return a URL for the Flickr image currently showing in the browser.
  
  The string parameter "kind" can be either "Short" or one of the standard
  Flickr image sizes: "Original", "Large", "Medium 640", "Medium", "Small",
  "Thumbnail", or "Square". If it's Short, the function will return a
  flic.kr URL for the image page. If it's one of the others, the function
  will return the URL of the image of that size, if available.
  
  The function works through Apple Events and supports only the Safari and
  Chrome browsers.'''
  
  # Flickr parameters
  fuser = 'Flickr username'
  key = 'Get key from Flickr'
  secret = 'Get secret from Flickr'
  
  # Make sure we're asking for a legitimate kind.
  kind = kind.capitalize()
  kinds = ["Short", "Original", "Large", "Medium 640",
           "Medium", "Small", "Thumbnail", "Square"]
  if kind not in kinds:
    return "Not a legitimate kind of URL"

  # Get the image ID.
  try:
    imageID = currentFlickrID()
  except IndexError:
    return "Not a Flickr image"
  
  # Establish the connection with Flickr.
  flickr = FlickrAPI(api_key=key, secret=secret)

  # Get the URL.
  if kind == "Short":
    return shorturl.url(photo_id = imageID)
  else:
    etree = flickr.photos_getSizes(photo_id = imageID, format = 'etree')
    for i in etree[0]:
      if i.attrib['label'] == kind:
        return i.attrib['source']
        break
  
    # If the size wasn't found.
    return "Size not found"


if __name__ == '__main__':
  print currentFlickrURL('Short')