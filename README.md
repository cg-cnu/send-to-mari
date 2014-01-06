# Send To Mari #
A handy way to send images to mari directly from file browser.

## Installation - Linux ##

### toggle_command_Port.py: ###
Toggles the command port in mari.
Place the script in the Scripts folder in the log path.
Creates a shortcut in python > toggle command port.

### Send_to_mari.py: ###
This script can be placed in any location.
To keep things organised you can place it in the same Scripts folder in the log path.
Make it executable.

### send_to_mari.desktop: ###
Place this .desktop file in the path 
/usr/share/services/ServiceMenus/

You might need to edit the following things in the script based on your paths...
Icon="The path where mari stores the icon"
*Run str(mari.resources.path('ICONS')) in mari and place the resulting path over here.

Exec="path/to/the/location/of/send_to_mari.py"
*Path to the send_to_mari.py file you have placed above.

### Reference ###
Refer to this kde tutorial for additional details on editing the .desktop file
http://techbase.kde.org/Development/Tutorials/Creating_Konqueror_Service_Menus

## Installation - Linux ##
Manually editing right click menu in windows is not a adviced.
You have to go through a bit of hackery.

Refer to this document for some information.
http://sbirch.net/tidbits/context_menu.html

## Usage ##

Launch mari.
Enable command port.
* if command port is enabled you will find a small plug icon in the bottom left corner in the viewport

Open Konqueror or Dolphin.
select image/images.
Right click > actions > Send To Mari.
All the selected images will be added to image manager in mari.