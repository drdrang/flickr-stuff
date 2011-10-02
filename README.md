# Flickr stuff #

  A set of scripts and libraries for working with Flickr on a Macintosh. They all require [Sybren Stüvel’s FlickrAPI library][2].

## getFlickrToken ##



getFlickrToken authorizes any program you've registered with Flickr (http://www.flickr.com/services/apps/create/) and puts its "token" in your `~/.flickr` directory. It's a command line program that your run with three arguments:

    1. The program's api key, which you get from Flickr.
    2. The program's api secret, which you get from Flickr.
    3. The program's permissions (read, write, or delete), which you determine.


## snapflickr ##

snapflickr takes a snapshot of your screen (similar to the builtin ⇧⌘4), saves a copy to your Desktop, and uploads a copy to your Flickr account. You provide a file name and (optionally) a description before taking the snapshot.

![snapflickr dialog box]( http://farm6.static.flickr.com/5074/5914101080_b6dc03beba_o.jpg)

It requires [Carsten Blüm's Pashua application][1] and its accompanying Python library. The use is described in more detail [here][3].

Near the top of snapflickr is a section of Flickr parameters:

    # Flickr parameters
    fuser = 'your Flickr username'
    key = 'get your key from Flickr'
    secret = 'get your secret from Flickr'
    screenshotsID = 'the ID of the Flickr set'

These must be customized with the appropriate username, API info, and Flickr set ID.

## currentflickr.py ##

This is a Python library for getting the name or certain types of URL for the Flickr image currently showing in your browser (works only for Safari and Chrome—sorry, Firefox users). In addition to the FlickrAPI library, it also requires the [appscript library][4], which allows Python to handle Apple Events (like AppleScript).

I use the currentFlickrURL function to make TextExpander shell snippets that return the URLs for various sizes of an image and also to return an image's short Flickr URL (http://flic.kr/p/xxxxx).

Near the top of currentflickr.py is a section of Flickr parameters:

    # Flickr parameters
    fuser = 'Flickr username'
    key = 'Get key from Flickr'
    secret = 'Get secret from Flickr'

These must be customized with the appropriate username and API info.

## Flickr.textexpander ##

This is a plist of TextExpander shell snippets for getting various Flickr URLs of the image shown in the frontmost tab of the browser. The snippets use the currentflickr.py library, so it must be customized with the user's name and API credentials and installed where Python can find it. 

## download-flickr-image ##

A script that downloads the large version of the Flickr image currently showing in the browser window and saves it to the Desktop. The filename is the Flickr image title, with ".jpg" appended if necessary. This is intended to be called via FastScripts or a similar utility. It dings using the Glass sound if it succeeds and burps with the Basso sound if it fails.

To play the sounds, the script requires the free [Play Sound utility][5] from Microcosm Software.


[1]: http://www.bluem.net/en/mac/pashua/
[2]: http://stuvel.eu/flickrapi
[3]: http://www.leancrew.com/all-this/2011/07/screenshotupload-utility-now-with-flickr/
[4]: http://appscript.sourceforge.net/
[5]: http://microcosmsoftware.com/playsound/
