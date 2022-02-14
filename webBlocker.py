from datetime import *
from time import *

host_path = r"/etc/hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "https://www.facebook.com"]

while True:
    # if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,17):
    with open(host_path, "r+") as fileptr:
        content = fileptr.read()
        for website in websites:
            if website in content:
                pass
                print("web was blocked")
            else:
                for web_info in websites:
                    print(f"blocking {web_info}")
                fileptr.write(redirect + "    " + website + "\n")
    # else:
    #     with open(host_path,'r+') as file:
    #         content = file.readlines()
    #         file.seek(0)
    #         for line in content:
    #             if not any(website in line for website in websites):
    #                 file.write(line)
    #         file.truncate()
