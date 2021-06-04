"""
get basic information phone numbers

pip install phonenumbers
"""

import phonenumbers
from phonenumbers mport geocoder, carrier, timezone

def get_number(number_phone):
  information = phonenumbers.parse(str(number_phone))
  """
  get description phone number
  """
  print(geocoder.description_for_number(information,'en'))
  
  """
  get carrier
  """
  print(carrier.name_for_number(information, 'en'))
