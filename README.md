# Send To Mari
Send images to mari directly from file browser.

## Linux Installation

* Manual
    + Dowload the zip file and extract it to **~/Mari/Scripts**
    + Copy **send_to_mari.desktop** to **~/.kde/share/kde4/services**
    + Make **send_to_mari.py** executable.

* Tested on centos 7 KDE4

## Usage

+ Launch mari.
+ Enable command port.![CommadPort](https://raw.githubusercontent.com/cg-cnu/mariSublime/master/examples/CommandPort.16x16.png)
+ if command port is enabled you will find a small plug icon in the bottom left corner of the viewport.
+ Open Konqueror/Dolphin.
+ select image/images.
+ Right click > actions > Send To Mari.
+ All the selected images will be added to image manager in mari.

### Dependency

+ Uses Tkniter for displaying error warnings

### Reference
+ Refer to this kde tutorial for additional details on editing the .desktop file
    + http://techbase.kde.org/Development/Tutorials/Creating_Konqueror_Service_Menus

+ Editing the right click menu in windows
    + http://sbirch.net/tidbits/context_menu.html
    + http://www.howtogeek.com/howto/windows-vista/add-any-application-to-the-desktop-right-click-menu-in-vista/