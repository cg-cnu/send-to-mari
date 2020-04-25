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
+ Enable command port using `mari.app.enableCommandPort( not ( mari.app.commandPortEnabled() ) )`
+ if command port is enabled you will find a small plug icon in the bottom left corner of the viewport. ![CommadPort](https://user-images.githubusercontent.com/2767425/80058701-22323f00-8569-11ea-9da2-43586931d9e2.png) 
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
