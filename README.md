# simkuring_telegram_bot
Telegram Bot using python 2.7

Tested on python 2.7, in future will support python 3 too.

## How to run
Create file config.ini based on config.ini.example

Edit key using your bot api key,

Set limit with small value. Limit is used to prevent bot attack. use bigger value if you dont care about it (e.g 99999)

set sleep value for rest time before next request.

query_limit is limit request for unread message from telegram server (default 100)

timeout is timeout for long polling, is you want using short polling set value with 0

after setup config.ini run file bot.py

```
python2 bot.py
```

## How to develop bot module
Add your python file to folder modules/

Edit file \_\_init\_\_.py in modules folder and import your module

Edit file bot.py add your command in variable commandLists.

## License
GPL v3
