# DWM Status for X
Mainly developed for Suckless's [dwm](https://dwm.suckless.org/). dwm-status prints basic informations about the current environment.
- Current time and date
- Battery percentage
- Volume
- Multiple network interfaces lan ip display
- Wired and Wifi interfaces state
- External ip addresses

## Dependencies
- dwm-status depends on [siji-font](https://github.com/stark/siji) installed and used as default font.
- Python 3
- cURL

## Install
``` sh
$ git clone https://github.com/57r4n63r/dwm-status.git
$ makepkg -sic
$ mkdir ~/.config/dwm-status
$ cp config.template.ini ~/.config/dwm-status/config.ini
```

edit file ~/.config/dwm-status/config.ini for configurations

## Plugins

Plugins can be added in this directory:

```
$ ~/.config/dwm-status/Plugins
```

Refer to the exemple to create your own.
