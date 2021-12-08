from speedtest import Speedtest  # pip install speedtest-cli


speedTest = Speedtest()
print("donwload : ", speedTest.download())
print("upload :", speedTest.upload())
speedTest.get_servers([])
print("ping : ", speedTest.results.ping + " ms")
