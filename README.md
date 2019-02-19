# DWM Status for X
Mainly developed for Suckless's [dwm](https://dwm.suckless.org/). dwm-status prints basic informations about the current environment.
- current time and date
- battery percentage
- volume
- vpn status (on/off)
- connection type (wired or wifi)
- local and external ip addresses

## Dependencies
- dwm-status depends on [siji-font](https://github.com/stark/siji) installed and used as default font.
- Python 3
- cURL

![dwm-status](preview.png "Preview of dwm-status")

## Install
``` sh
$ git clone https://github.com/57r4n63r/dwm-status.git
$ makepkg -sic
```
