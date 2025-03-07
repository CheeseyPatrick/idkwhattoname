import re
import discord
from discord.ext import commands
import pyautogui
import threading
# pip install discord.py-self pyautogui

#--------------------------------#
# optionss
CHANNEL = 1304836669043773571 # this is the channel id of where you are expecting the link to be sent. 1304836669043773571 is RT-Brainrotteds #announcements as of 3/7/25
TOKEN = "MTMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # this is the token of your discord account. do not share this with anyone!
#--------------------------------#

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="==!", self_bot=True, help_command=None)

    async def on_ready(self):
        print(f'{GREEN}Logged on as {self.user}{RESET}')
        channel = self.get_channel(CHANNEL)
        print(f'{GREEN}Watching for messages in {RED}{channel.guild.name}{GREEN}: {RED}#{channel.name}{RESET}')
        print('''
              1. Make sure you have Brawl Stars open and focused. 
              2. Click on the text input area where you can type the join code for a team. 
              3. Then, without clicking anything else, hover over the join button.
            ''')
        
    def type_it(self, text):
        pyautogui.typewrite(str(text), 0.01)
        pyautogui.click()
    
    def extract_party_id(self, text):
        pattern = r"tag=([A-Z0-9]+)"
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        return None

    async def on_message(self, message: discord.Message):
        if (message.channel.id == CHANNEL) and len(party_id := self.extract_party_id(message.content)) > 0: # 🦭 walrus moment
            thread = threading.Thread(target=(self.type_it), args=(party_id,), daemon=True)
            thread.start()
    
client = MyClient()
client.run(token=TOKEN)
