from configparser import ConfigParser

config = ConfigParser()

config["GRAPHIC"] = {
    "width": 800,
    "height": 1000,
    "offset": 50
}

with open("config/lsystem_deafult.ini", "w") as f:
    config.write(f)