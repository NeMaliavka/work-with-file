import requests
import time

def find_uk_city(coordinates: list) -> str:
    # API = '65ae97b123696043220487avude3e26'
    URL = 'https://geocode.maps.co/reverse?'

    uk_city = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']

    for lat, lon in coordinates:
        response = requests.get(f'{URL}lat={lat}&lon={lon}')
        data = response.json()
        city = data.get('address', {}).get('city')

        if city in uk_city:
            return city
        else:
            time.sleep(1)
            continue


if __name__ == '__main__':
    _coordinates = [
        ('48.2083537', '16.3725042'),
        ('52.628606', '1.29227'),
        ('55.7514952', '37.618153095505875')
    ]

    print(find_uk_city(_coordinates))

    # try:
    #     assert find_uk_city(_coordinates) == 'Liverpool'
    #     assert find_uk_city(_coordinates) == 'Norwich'
    #     assert find_uk_city(_coordinates) == 'Oxford'
    # except AssertionError:
    #     print('no city')
