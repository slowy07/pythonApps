#before run
#pip install  -r requirements.txt
import psutil #pip install psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent


if percent >= 30:
    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification

    Notification(
        title = "Battery Low"
        description = str(percent) + "% Battery Remain !"
        duration = 5
        urgency = Notification.URGENCY_CRITICAL
    ).send()