import os
import random
import threading
import requests
from pystyle import *
import time
import sys
import datetime
import socket
class MainSHare:
    def __init__(self):
        self.blue = Col.light_blue
        self.lblue = Colors.StaticMIX((Col.light_blue, Col.white, Col.white))
        self.red = Colors.StaticMIX((Col.red, Col.white, Col.white))
        try:
            self.open_file = open('token.txt').read().split('\n')
            self.open_file.remove('')
            self.total = str(len(self.open_file))
        except:
            quit(self.format_print("$", 'No Such File "token.txt"'))
    def format_print(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.lblue, self.blue)} {self.lblue}{text}{Col.reset}"""
    def format_input(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.red, self.blue)} {self.red}{text}{Col.reset}"""
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        title = '\n\n\n--By [\] Thanh Sang '
        banner = '''\n \n [\] Tran Thanh Sang\n\n'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_gray)), Center.XCenter(title+'Token: '+self.total)) + Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner)))
        if self.total == '0':
            quit(self.format_print("[\]", "Không Có Token Hợp Lệ !"))
    def share(self, id_post, token):
        rq = random.choice([requests.get, requests.post])
        dt_now = datetime.datetime.now()
        response = rq(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
        if 'id' in response:
            print(self.format_print("Tran Thanh Sang",f"{dt_now.strftime('%H:%M:%S')}: {response['id']}"))
        else:
            print(self.format_print("Tran Thanh Sang",f"{dt_now.strftime('%H:%M:%S')}: SHARE POST FAILED!"))
    def run_share(self):
        while True:
            main.banner()
            try: 
                id_post = input(self.format_input("!",f"ID Bài Viết : "))
                threa = int(input(self.format_input("!",f"INPUT Số Luồng : ")))
                if id_post != '' and threa > 0:
                    break
                else:
                    print(self.format_print("#", "Luồng > 0!"))
                    time.sleep(3)
            except:
                print(self.format_print("#", "Luồng INT!"))
                time.sleep(3)
        while True:
            for token in self.open_file:
                t = threading.Thread(target=self.share, args=(id_post, token))
                t.start()
                while threading.active_count() > threa:
                    t.join()
if __name__ == "__main__":
    try:
        main = MainSHare()
        main.run_share()
    except KeyboardInterrupt:
        time.sleep(3)
        sys.exit('\n'+main.format_print('*', 'Good Bye:)'))
