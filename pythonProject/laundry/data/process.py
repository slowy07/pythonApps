import datetime
import csv


timenow = datetime.datetime.now()

class user:
    def __init__(self, name, information)->str:
        self.name = name
        self.information = information

    def get_username(self) ->str:
        return self.name
    
    def get_user_information(self) ->str:
        return self.information
    
class laundryinfo:
    def __init__(self):
        self.time = datetime.datetime.now()

    def calculate(self, laundry_weight) -> str:
        total = laundry_weight * 5000
        
        return f"Harga total : Rp.{total}"

    def get_time(self) -> str:
        timeNow = self.time.strftime('%H:%M')
        
        return f"waktu : {timeNow}"

user_info = user('arfy', 'baju 4 kg')
harga = laundryinfo().calculate(4)
waktu_skrng = laundryinfo().get_time()
print(user_info.get_username())
print(user_info.get_user_information())
print(harga)

def save_data():
    filename = f"laundry_{timenow.strftime('%d-%B-%Y')}.txt"
    text_information = f"desc :{user_info.get_user_information()}\nnama : {user_info.get_username()}\nharga : {harga}\nwaktu:{waktu_skrng}\n\n"
    save_data_log = open(filename, 'a')
    save_data_log.write(text_information)
    save_data_log.close()
    print('saved')

save_data()

    
