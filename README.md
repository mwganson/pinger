## Pinger Macro
A FreeCAD forum user pinger macro and html version

## Background
The FreeCAD [forum](https://forum.freecadweb.org) is run on [phpBB](https://www.phpbb.com/) and lags behind other modern forum software niceties and conveniences. One is the ability to easily `@mention` other users in the forum. One must tediously reference an other user's `user_id` and add manually add it to:
`[quote=username user_id=1234]ping[/quote]`  
Note: Although, there is a [PR](https://github.com/phpbb/phpbb/pull/5225) in the phpBB git repo to add @mentions in to the source code, it has been stalled for several years. Therefore this macro was created to simply the experience for forum moderators and frequent forum users.

## Usage

## Install

1. From your FreeCAD Macros folder open a git bash terminal and enter:  
`git clone https://github.com/mwganson/pinger.git`

2. This creates a subfolder inside your FreeCAD Macros folder called `pinger`, e.g:
`Linux/MacOS: ~/.FreeCAD/Macros/pinger/`
`Windows:     c:\users\username\Documents\Macros\pinger`
3. Inside the `pinger/` folder you will find `pinger_launcher.py`.  Copy that file up into the Macros folder and run it to run the macro.
`Note:` `pinger_launcher.py` is a very simple file that simply launches the macro.  It should not have any additional changes, and so won't need to be updated, presumably.  If it does get updated you would need to replace the file in your Macros folder with the new launcher.  
4. This change enables you to update the macro by opening a git bash terminal in the Macros/pinger folder and using:
`git pull`

There is also a `pinger.html` file if you want to run the javascript version, which has the nice feature of allowing you to add custom users and stores them as a sort of cookie in localstorage inside your browser.

Note: User chrisb has made some changes to the user interface allowing for multiple selection, which I have uploaded as `pinger2.html`.
