import telebot
import config
from gpt_utilites import GPT_utilities

class Bot:
    
    def __init__(self):
        self.bot = telebot.TeleBot(config.telebot_token)
        self.gpt = GPT_utilities()
        
    def mainloop(self):
        
        @self.bot.message_handler(commands=['start', 'gpt', 'config', 'image'])
        def main_commands(msg):
            if msg.from_user.id not in config.my_accs:
                self.bot.send_message(msg.from_user.id, 'You are not me')
                print(msg.from_user.id)
                return
            if msg.text.startswith('/gpt'):
                user_input = msg.text[5:].split('\n#\n')
                if len(user_input) == 1:
                    response = self.gpt.get_response(user_input[0])
                    self.bot.send_message(msg.from_user.id, response)
                elif len(user_input) == 2:
                    prompt = user_input[0]
                    settings = self.parse_settings(user_input[1])
                    response = self.gpt.get_response(prompt, **settings)
                    self.bot.send_message(msg.from_user.id, response)
            elif msg.text.startswith('/config'):
                pass
            elif msg.text.startswith('/image'):
                pass
            
        self.bot.polling(none_stop=True)
    
    def parse_settings(self, user_input):
        settings = {}
        for setting in user_input.split('\n'):
            data = setting.split(': ')
            if data[0] == 'model':
                settings['model'] = data[1]
            elif data[0] == 'temperature':
                settings['temperature'] = float(data[1])
            elif data[0] == 'max_length':
                settings['max_length'] = int(data[1])
            elif data[0] == 'frequency_penalty':
                settings['frequency_penalty'] = float(data[1])
            elif data[0] == 'presence_penalty':
                settings['presence_penalty'] = float(data[1])
            else:
                print('Error: Unknown setting: {}'.format(data[0]))
        return settings  

if __name__=="__main__":
    bot = Bot()
    bot.mainloop()
