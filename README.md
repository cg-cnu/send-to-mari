# Send To Mari #
A handy way to send images to mari directly from file browser.

## Installation - Linux ##

### toggle_command_Port.py: ###
<br>Toggles the command port in mari.
<br>Place it in the Scripts folder in the log path.
<br>Creates a shortcut in the menu: python > toggle command port.

### Send_to_mari.py: ###
<br>It can be placed in any location.
<br>To keep things organised you can place it in the same Scripts folder in the log path.
<br>Make it executable.

### send_to_mari.desktop: ###
<br>Place this .desktop file in the path 
<br>/usr/share/services/ServiceMenus/

<br>You might need to edit the following things in the script based on your paths...

<br>Icon="The path where mari stores the icon"
<br>*Run str(mari.resources.path('ICONS')) in mari and place the resulting path over here.

<br>Exec="path/to/the/location/of/send_to_mari.py"
<br>*Path to the send_to_mari.py file you have placed above.

### Reference ###
<br>Refer to this kde tutorial for additional details on editing the .desktop file
<br>http://techbase.kde.org/Development/Tutorials/Creating_Konqueror_Service_Menus

## Usage ##

<br>Launch mari.
<br>Enable command port.
<br>if command port is enabled you will find a small plug icon in the bottom left corner in the viewport

<br>Open Konqueror or Dolphin.
<br>select image/images.
<br>Right click > actions > Send To Mari.
<br>All the selected images will be added to image manager in mari.
