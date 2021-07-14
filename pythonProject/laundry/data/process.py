import datetime

timenow = datetime.datetime.now()


class user:
    def __init__(self, name, information) -> str:
        self.name = name
        self.information = information

    def get_username(self) -> str:
        return self.name

    def get_user_information(self) -> str:
        return self.information


class laundryinfo:
    def __init__(self):
        self.time = datetime.datetime.now()

    def calculate(self, laundry_weight, type_of_laundry) -> str:
        cuci_komplit = 6000
        cuci_kering = 4000
        setrika = 4000
        bed_cover = 8000
        # selimut = 7000
        # gorden = 7000
        express = 9000

        if type_of_laundry in ["selimut", "gorden"]:
            type_of_laundry = 7000
        elif type_of_laundry == "cuci komplit":
            type_of_laundry = cuci_komplit
        elif type_of_laundry == "cuci kering":
            type_of_laundry = cuci_kering
        elif type_of_laundry == "setrika":
            type_of_laundry = setrika
        elif type_of_laundry == "bed cover":
            type_of_laundry = bed_cover
        elif type_of_laundry == express:
            type_of_laundry = express

        total = type_of_laundry * int(laundry_weight)

        return int(total)

    def get_time(self) -> str:
        timeNow = self.time.strftime("%H:%M")

        return f"waktu : {timeNow}"


def save_data():
    filename = f"laundry_{timenow.strftime('%d-%B-%Y')}.txt"
    text_information = f"desc :{user.get_user_information()}\nnama : {user.get_username()}\nharga : price\nwaktu: time\n\n" # lgtm [py/call/wrong-arguments]
    save_data_log = open(filename, "a")
    save_data_log.write(text_information)
    save_data_log.close()
    print("saved")