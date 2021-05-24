# Мониторинг системы
* [conky](https://ru.wikipedia.org/wiki/Conky)

![картинка](https://upload.wikimedia.org/wikipedia/commons/e/e3/Conky_rus.png)
## Установка 
```
# Устанавливаем conky
sudo pacman -S conky
```
## Автозагрузка
```
# Создаем сервис
sudo touch ~/.config/autostart/conky.desktop
sudo nano ~/.config/autostart/conky.desktop

# Заполняем файл сервиса
[Desktop Entry]
Encoding=UTF-8
Version=0.9.4
Type=Application
Name=conky
Comment=System monitor
Exec=/mnt/0/documents/projects/conky/scripts/conky_scheduler.sh
StartupNotify=false
Terminal=false
Hidden=false
```
* [neofetch](https://losst.ru/neofetch-informatsiya-o-sisteme-linux-i-logotip-v-terminale)

![картинка](https://camo.githubusercontent.com/baa2dbda5355e2659de7338d3a53a7783ca9071d/68747470733a2f2f692e696d6775722e636f6d2f6c55726b51424e2e706e67)
```
# Устанавливаем neofetch 
sudo pacman -S neofetch
```
* [htop](https://ru.wikipedia.org/wiki/Htop)

![картинка](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Htop_on_a_48_core_computer.png/274px-Htop_on_a_48_core_computer.png)
```
# Устанавливаем htop 
sudo pacman -S htop
```

## Балансы
Балансы получаю через [API flask.](https://github.com/VolokzhaninVadim/flask)
