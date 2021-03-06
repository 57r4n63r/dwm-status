
class Icons:
    items = {
            "fullsquare":"\ue000",
            "bordersquare":"\ue001",
            "listing1":"\ue002",
            "listing2":"\ue003",
            "bluetooth":"\ue00b",
            "usb":"\ue00c",
            "power":"\ue00d",
            "archlinux":"\ue00e",
            "pacman":"\ue00f",
            "pacman_ghost":"\ue0c6",
            "clock1":"\ue017",
            "clock2":"\ue018",
            "shuriken":"\ue027",
            "signalbars_poor":"\ue047",
            "signalbars_good":"\ue048",
            "wired":"\ue19e",
            "wifi_poor":"\ue049",
            "wifi_medium":"\ue04a",
            "wifi_good":"\ue04b",
            "microphone":"\ue04c",
            "headphones":"\ue04d",
            "speaker":"\ue04e",
            "speaker_mute":"\ue04f",
            "email":"\ue121",
            "dwm":"\ue241",
            "battery_pluged":"\ue23e",
            "battery_unpluged":"\ue23f",
            "console":"\ue1ec",
            "shield":"\ue1f7",
            "home":"\ue1f0",
            "globe":"\ue1a0",
            "meteo_cloudy":"\ue22b",
            "meteo_lightning":"\ue22c",
            "meteo_rain":"\ue22d",
            "meteo_snow":"\ue22e",
            "meteo_rainshower":"\ue22f",
            "meteo_cloudy_sunny":"\ue231",
            "meteo_sunny":"\ue234",
            "meteo_windy":"\ue235"
            }
    @staticmethod
    def get(name):
        if name in Icons.items:
            return Icons.items[name]
        else:
            return ''
