# before run
# pip install  -r requirements.txt
import psutil  # pip install psutil
from plyer import notification

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    notification.notify(
        title="Battery Percentage",
        message=str(percent) + "% Battery remaining",
        timeout=10,
    )
    continue
