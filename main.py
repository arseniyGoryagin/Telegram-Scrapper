
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon import functions, types, errors
from telethon.tl.types import User
import os
import sys

load_dotenv()

api_id : str = os.getenv("TELEGRAM_API_ID")
api_hash_id : str = os.getenv("TELEGRAM_API_HASH")
phone_number : str = os.getenv("TELEGRAM_PHONE_NUMBER")
target_chat_name : str = os.getenv("TARGET_CHAT")
target_file : str = os.getenv("TARGET_FILENAME")

client = TelegramClient("session", api_id, api_hash_id)
client.start(phone_number)



def get_chat_from_name(chat_name :str) -> str:

    dialogs = client.get_dialogs()

    for dialog in dialogs:
        if dialog.name == chat_name:
            if dialog.is_channel == True:
                continue
            return dialog


    return None 
     



def main():

    target_chat = get_chat_from_name(target_chat_name)

    if(target_chat == None):
        print("No such chat")
        return 



    participants = []

    for participant in client.iter_participants(target_chat.entity.id):
        if isinstance(participant, User):
            participants.append(participant)


    

    with open(target_file, 'w')as file:
        for participant in participants:
            if(participant.username != None):
                file.write(participant.username + "\n")



main()