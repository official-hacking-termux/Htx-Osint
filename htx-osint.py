import requests

API_KEY = "d6d4ad6e4c0a811b6250ee2fbb373c10"  # Numverify.com se free key le lo

def get_number_details(number):
    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}"
    r = requests.get(url)
    data = r.json()
    if data.get("valid"):
        print(f"Number: {data['international_format']}")
        print(f"Country: {data['country_name']}")
        print(f"Location: {data['location']}")
        print(f"Carrier: {data['carrier']}")
        print(f"Line Type: {data['line_type']}")
    else:
        print("Invalid number or no data.")

num = input("Enter number with country code (+91...): ")
get_number_details(num)
