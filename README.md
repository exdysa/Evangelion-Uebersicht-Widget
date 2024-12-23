# Evangelion-Übersicht-Widget

This is a widget for [Übersicht](http://tracesof.net/uebersicht/).

It looks like this:

![A screenshot of a MacOS desktop with a black and white hex pattern decoring the lower left and upper rightcorners](https://github.com/exdysa/Evangelion-Uebersicht-Widget/blob/f28d300caaaf8605a63175b134e557e49cff1349/screenshot2.png)

I encountered some server errors with the original project, and in the process I learned the original shell scripts of this widget were writing countless files to my hard drive.

I cannot accept this behavior.
The system status routines are now tidy and translated to Python, which is included with all MacOS systems.

* Setup
	* Install [Übersicht](http://tracesof.net/uebersicht/)
	* Download the [widget archive](https://raw.githubusercontent.com/exdysa/Evangelion-Uebersicht-Widget/NERV/EVA_ueber-widget.py.zip)
	* Move this widget into Übersicht folder.
	* Thank you for looking forward to it!

## Instruction

Übersicht's `Preferences...` menu has `Interaction : Enable Interaction` checked by default. Please ensure this is so if you want to click the widget tiles.

## Supported Languages

* Deutsch
* English

## Features
- Memory pressure levels (NORMAL, WARN, CRITICAL)

*  **NORMAL:** Everything is fine. No performance issue!
*  **WARN:** There might a be noticeable drop in performance.
*  **CRITICAL:** The computer will likely freeze up, and the user should terminate some processes.

- CPU Usage
- Battery level
- Time
- Network traffic
- Public IP Address

- Now Playing and music player controls for iTunes
- Icons for up to 5 Mounted volumes
- Optional voice alerts (off by default)
- Update notification
- CPU Utilization / Low Battery alarm
- Trash size and Empty trash

### Contact
* [Open a new issue to provide enhancement suggestions, identify difficulties, or share feedback!](https://github.com/exdysa/Evangelion-Uebersicht-Widget/issues)

* [Contact the original author ](jetic@me.com)

<details ><summary>

## Original Changelog

</summary>

**0.X14.4a**
* Attempting to fix iTunes for Catalina

**0.X14.3a**
* Bug fix for DoNotDisturb

**0.X14.2a**
* Changed how all commands are executed to save energy.

**0.X14.1a**
* Optimisation.

**0.X14.0a**
* Optimisation.

**0.X13a**
* Changed the CPU script.

**0.X12a**
* Changed the networking script to only monitor main network interface.

**0.X11a**
* Now monitoring memory pressure, since memory percentage does not make sense for macOS

**0.X10a**
* Added option to not show the update button

**0.X9a**
* Update now preserves customised settings (starting from next update)

**0.X8a**
* Display an update button when there are new versions available

**0.X7a**
* Fixing a minor bug with iTunes cell

**0.X6a**
* Fixing a minor bug with iTunes cell

**0.X5a**
* Fixed a minor bug with battery alert

**0.X4b**
* Fixed a few minor bugs with the scripts
* Fixed a bug with desktop computers
* Added the option to change colours
* Added a lot of options to customise the widget
* Added voice notifications. Default option is OFF to avoid annoyance.

**0.X3a**
* Fixed a few interface issues.
* Updated a few lines of comments.

**0.X2a (Major Update!)**
* This is probably the most important update since 0.5a. I added some major improvements to make it faster and fixed a lot of ages old bugs, and most importantly the energy consumption problem.

**0.X1a**
* This new version includes a lot of migration from commands to scripts to improve performance and potentially, decrease energy demand. I want to experiment with some new ideas to make it more battery and CPU friendly.

**0.Xa**
* Removed language support for Traditional Chinese
* Added support to adjust the size of widget(By using font-size. All sizes are specified in em instead of px now.)
* Fixed a bug where network display and iTunes might malfunction.

**0.98a**
* Fixed a compatibility issue with Sierra's removal of sar

**0.97a**
* Fixed a bug with battery remain

**0.96a**
* Fixed a bug with battery alert

**0.95a**
* Fixed a bug with battery display

**0.94a**
* Resolving compatibility issue with OSX Sierra

**0.93a**
* Fixed a bug with DoNotDisturb alert

**0.92a**
* Fixed a bug with DoNotDisturb alert

**0.91a**
* Fixed a bug with DoNotDisturb alert

**0.90a**
* Add DoNotDisturb alert
* Fixed a bug with multi-language support

**0.89a**
* Fixed a UI problem with newer versions of übersicht.
* Changed iTunes to SEELE, it looks better.

**0.88a**
* Added iTunes Album cover display.
* Fixed a bug where disk cell might not function properly.

**0.87a**
* Fixed a bug with time display on new version of übersicht.

**0.86a**
* Fixed a bug with network traffic cells.

**0.85a**
* Fixed a bug with Empty Trash function, contributed by @mgarbacz

**0.84a**
* Added random delay of warning cells. Special thanks to NorthIsUp.

**0.83a**
* Added two blocks to show the sum of network traffic on all interfaces, notice that it includes localhost2localhost traffic.

**0.82a**
* Fixed an issue with disk displaying when the computer doesn't have an installed battery

**0.81a**
* Fixed an issue with battery displaying when the computer doesn't have an installed battery

**0.8a**
* Modified the design of warning cell, it looks cooler
* Adjusted the line height of output cell
* Modified the render mechanism to execute less commands when updating

**0.71a**
* Fixed a bug while iTunes Cell might not display contents correctly under Yosemite

**0.7a**
* Added Multi-language support, currently supporting English, German and Chinese

**0.63a**
* Added title and artist displaying on iTunes cell

**0.62a**
* Added function, now you can open up a volume by clicking!

**0.61a**
* Fixed bug where non-system volumes might be shown as a system volumes. If one is still experiencing irregularities with their volumes one could try ls /Volumes/ command in Terminal
* Added comments

**0.6a**
* Added mounted volumes display, currently displaying the first 5 volumes in /Volumes/
* Changed Output cell to display original outputs without uppercasing transformation

**0.52a**
* Added function: empty trash on clicking the trash cell

**0.51a**
* Fixed a bug, where it used to show countdown when not supposed to

**0.5a**
* Added left-bottom corner panel
* Added iTunes remote cell

**0.45a**
* Fixed problem with the hovering effect of IPCell
* Change from Simplified Chinese to Traditional (This is actually a mistake I made in the early phase of coding)

**0.44a**
* Fixed IP displaying when there’s no internet connection

**0.43a**
* Bug fix for OSX 10.10 (mine is 10.11)

**0.42a**
* Improved alarm, bug fixed
* Added animation to alarm

**0.41a**
* Added blinking when alert triggered

**0.4a**
* Added alert system, will alert when battery is below 20% or when CPU usage reaches 90%
* restructured the code, added comments

**0.3a**
* Added Memory and CPU usage
* Colour scheme changed
* Error message changed

**0.22a**
* Improved Trash Issue
* Output cells enabled, press on cell 32 and information will popup

**0.22a**
* Improved Trash Issue
* Output cells enabled, press on cell 32 and information will popup

**0.21a**
* Fixed Trash

**0.2a**
* Fix battery hover

**0.1a**
* Added General UI
* Added Battery
* Added Time and Day
</details>