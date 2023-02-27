# System monitoring
* [conky](https://ru.wikipedia.org/wiki/Conky)

![conky_icon.png](conky_icon.png)

![screenshot.png](screenshot.png)

## Install Arch Linux
```
# Install conky
sudo pacman -S conky
```
## Autoload
```
# Create service
sudo touch ~/.config/autostart/conky.desktop
sudo nano ~/.config/autostart/conky.desktop

# Fill service file
[Desktop Entry]
Encoding=UTF-8
Version=0.9.4
Type=Application
Name=conky
Comment=System monitor
Exec=/mnt/0/documents/projects/pc_settings/conky/scripts/conky_scheduler.sh
StartupNotify=false
Terminal=false
Hidden=false
```
* [neofetch](https://losst.ru/neofetch-informatsiya-o-sisteme-linux-i-logotip-v-terminale)

![img](https://camo.githubusercontent.com/baa2dbda5355e2659de7338d3a53a7783ca9071d/68747470733a2f2f692e696d6775722e636f6d2f6c55726b51424e2e706e67)
```
# Install neofetch Arch Linux
sudo pacman -S neofetch
```
* [cpufetch](https://github.com/Dr-Noob/cpufetch)
![img](https://github.com/Dr-Noob/cpufetch/raw/master/pictures/examples.gif)
```
# Install cpufetch Arch Linux
yay -S cpufetch-git  
```

* [htop](https://ru.wikipedia.org/wiki/Htop)

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Htop_on_a_48_core_computer.png/274px-Htop_on_a_48_core_computer.png)
```
# Insatll htop Arch Linux
sudo pacman -S htop
```
