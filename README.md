# Flickr stuff #

  A set of scripts and libraries for working with Flickr on a Macintosh. They all require [Sybren Stüvel’s FlickrAPI library][2].

## getFlickrToken ##



getFlickrToken authorizes any program you've registered with Flickr (http://www.flickr.com/services/apps/create/) and puts its "token" in your `~/.flickr` directory. It's a command line program that your run with three arguments:

    1. The program's api key, which you get from Flickr.
    2. The program's api secret, which you get from Flickr.
    3. The program's permissions (read, write, or delete), which you determine.


## snapflickr ##

snapflickr takes a snapshot of your screen (similar to the builtin ⇧⌘4), saves a copy to your Desktop, and uploads a copy to your Flickr account.

When snapflickr is run, it turns the cursor into a camera, ready to take a snapshot of any window (you can change it to take a snapshot of an arbitrary rectangle by pressing the spacebar). After the snapshot is taken, a window appears in which you provide a file name and (optionally) a description.

![snapflickr dialog box](http://farm8.staticflickr.com/7065/6773443376_b9d6f3dd48_o.jpg)

By default, the snapshot is uploaded to your Flickr account, but if you click the "Local file only" checkbox, there's no upload. If the image is uploaded to Flickr, its page is opened in the default browser and an `<img>` tag for the chosen size is put on the clipboard.

It requires [Carsten Blüm's Pashua application][1] and its accompanying Python library. The use is described in more detail [here][3]. It also requires the [Python Imaging Library][6] to add a desktop background color to window screenshots.

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

## up2flickr ##

A script that uploads a list of images to Flickr. The title on Flickr is the file name minus the extension. The images are private by default but can be made public through a command line option.

Near the top of up2flickr is a section of Flickr parameters:

    # Flickr parameters
    fuser = 'Flickr username'
    key = 'Get key from Flickr'
    secret = 'Get secret from Flickr'

These must be customized with the appropriate username and API info.



[1]: http://www.bluem.net/en/mac/pashua/
[2]: http://stuvel.eu/flickrapi
[3]: http://www.leancrew.com/all-this/2012/02/snapflickr-update/
[4]: http://appscript.sourceforge.net/
[5]: http://microcosmsoftware.com/playsound/
[6]: http://www.pythonware.com/products/pil/
