# pinger
FreeCAD forum user pinger macro and html version

To install:

From your Macros folder open a git bash terminal and enter:

<pre>git clone https://github.com/mwganson/pinger.git</pre>

This creates a subfolder inside your Macros folder called pinger, e.g.:

c:\users\username\Documents\Macros\pinger

Inside the pinger folder you will find pinger_launcher.py.  Copy that file up into the Macros folder and run it to run the macro.

Note: pinger_launcher.py is a very simple file that simply launches the macro.  It should not have any additional changes, and so won't need to be udpated, presumably.  If it does get updated you would need to replace the file in your Macros folder with the new launcher.  

This change enables you to update the macro by opening a git bash terminal in the Macros/pinger folder and using:

<pre>git pull</pre>

There is also a pinger.html file if you want to run the javascript version, which has the nice feature of allowing you to add custom users and stores them as a sort of cookie in localstorage inside your browser.
