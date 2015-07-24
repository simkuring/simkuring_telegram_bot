import requests
from time import sleep
import json
import ConfigParser
import modules

# config
config = ConfigParser.ConfigParser()
config.read("config.ini")
key = config.get("setting","key")
limit = config.getint("setting","limit")
sleepTime = config.getint("setting","sleep")
queryLimit = config.getint("setting","query_limit")
timeout = queryLimit = config.getint("setting","timeout")

# set url
headers = {"Content-type": "application/x-www-form-urlencoded"}
url = "https://api.telegram.org/bot"
sendMsgUrl = url + key + "/sendMessage"
getMsgUrl = url + key + "/getUpdates"

# help and about    
def help(args):
    return """
        /jam
        /adzan [bandung, bogor, jakarta, aceh, samarinda, balikpapan, makassar]
        /ddg [keyword]
        /about
    """

def about(args):
    about = """
        Bot Simkuring v .1 alpha by Simkuring Laboratory
    """
    return about

# bot command list + function
commandLists = {
    "/jam":modules.jam,
    "/adzan":modules.adzan,
    "/ddg":modules.ddg,
    "/about":about,
    "/help":help
}

def sendMessage(chatId, msgId, text):
    try:
        data = {"chat_id":chatId,"text":text,"reply_to_message_id":msgId}
        r = requests.post(sendMsgUrl,data=data)
        if r.status_code != 200:
            print r.status_code
    except:
        print "weee"
    
def parseCommand(msg):
    panjang = len(msg['result'])
    for i in range(panjang):
        try:
            perintah = msg['result'][i]['message']['text'].replace("@SimkuringBot","")
            command = perintah.split()
            if command[0] in commandLists.keys():
                data = commandLists[command[0]](command)
                sendMessage(msg['result'][i]['message']['chat']['id'], msg['result'][i]['message']['message_id'], data)
        except:
            pass
    
def main():
    lastMessageId = 0;
    while (True):
        data = {
            "offset":lastMessageId,
            "timeout":timeout,
            "limit":queryLimit
        }
        bot = requests.post(getMsgUrl,data=data)
        if bot.status_code == 200:
            msg = bot.json()
            panjang = len(msg['result'])
            if panjang > 0 :
                if panjang < limit :
                    parseCommand(msg)
                lastMessageId = msg['result'][panjang-1]['update_id'] + 1
        else:
            print bot.status_code
        sleep(sleepTime)

if __name__ == "__main__":
    main()