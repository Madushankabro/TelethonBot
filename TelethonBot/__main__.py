# @DamienSoukara

import glob
from pathlib import Path
from TelethonBot.utils import load_plugins
import logging
from . import Alty

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "TelethonBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @DamienSoukara")

if __name__ == "__main__":
    Alty.run_until_disconnected()
