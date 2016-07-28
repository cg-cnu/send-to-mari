# Send To Mari
Send images to mari directly from file browser.

## Linux Installation

* Script
    +
    + Run setup.sh

* Manual
    + toggle_command_Port.py:
        + Creates a shortcut in the menu: python > toggle command port.
        + It enables/disables the command port in mari.
        + Place it in **~/Mari/Scripts**.

    * Send_to_mari.py:
        + It can be placed in any location.
        + To keep things organised you can place it in the same Scripts folder(~/Mari/Scripts).
        + Make it executable.

    * send_to_mari.desktop:
        + Place this .desktop file in the path /usr/share/services/ServiceMenus/
        + You might need to modify the following lines in the .desktop file
        + Icon="The path where mari stores the icon"
        + Run str(mari.resources.path('ICONS')) in mari and place the resulting path over here.
        + Exec="path/to/the/location/of/send_to_mari.py"
        + Path to the send_to_mari.py file you have placed above.

* Tested on centos 7

## Windows

+  For windows we don't use .desktop file.
+  Manually editing right click in windows require a bit of hacking.
+  I suggest you go through the links given in the reference section.

## Usage
+ Once you have successfully installed.
+ Launch mari.
+ Enable command port.
+ *if command port is enabled you will find a small plug icon in the bottom left corner of the viewport
+ Open Konqueror/Dolphin or Windows Explorer.
+ select image/images.
+ Right click > actions > Send To Mari.
+ All the selected images will be added to image manager in mari.

### Reference ###
+ Refer to this kde tutorial for additional details on editing the .desktop file
+ http://techbase.kde.org/Development/Tutorials/Creating_Konqueror_Service_Menus

+ Refer to this for editing the right click menu in windows
+ http://sbirch.net/tidbits/context_menu.html
+ http://www.howtogeek.com/howto/windows-vista/add-any-application-to-the-desktop-right-click-menu-in-vista/