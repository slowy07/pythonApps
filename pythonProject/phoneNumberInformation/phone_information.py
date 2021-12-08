"""
get basic information phone numbers

pip install phonenumbers
"""

import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def get_number(number_phone):
    information = phonenumbers.parse(str(number_phone))
    """
  get description phone number
  """
    print(geocoder.description_for_number(information, "en"))

    """
  get carrier
  """
    print(carrier.name_for_number(information, "en"))

    # get timezone
    print(timezone.time_zones_for_number(information))


phone_number = input("Enter phone number")
print("get phone number")

get_number(phone_number)
