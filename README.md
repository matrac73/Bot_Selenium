# Bot_Selenium

Objectif : Créer des bots afin d'interagir avec des site web

## Présentation du dépot
### Architecture GIT

    .
    ├── .gitignore                      # avoid unecessary data exchange between git and local files
    ├── bots                                  
    │   ├── Kahoot                        
    │   │   └── bot_kahoot.py           # bot connecting several accounts simultaneously to one kahoot game
    │   ├── Instagram
    │   │   └── bot_insta.py            # bot liking multiple posts on instagram
    │   └── Dactylo
    │       └── bot_dactylo.py          # bot typing very fast the words on a dactylography game online
    ├── README.me                       # presents the GIT repository
    └── drivers
        ├── geckodriver.exe             # browser driver for firefox
        └── chromedriver.exe            # browser driver for google chrome

## Setup du projet

1 . Se placer dans le répertoire local dans lequel on veut importer le dépot git :
``` bash
cd ./path/to/repository/
```
5 . Cloner le dépot git :
``` bash
git clone https://github.com/matrac73/Bot_Selenium.git
```
6 . Se placer dans le répertoire qui viens d'être crée :
``` bash
cd ./Bot_Selenium/
```
7 . Ajouter les driver au PATH de l'ordinateur :

Suivre le tutoriel de ce site web : https://java.com/fr/download/help/path.html

6 . Lancer le bot (kahoot par exemple):
``` bash
python ./bots/Kahoot/bot_kahoot.py
```
