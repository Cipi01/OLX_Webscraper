import glob
import os

import pandas as pd

from dicts import brand_list_auto, brand_list_moto
from unidecode import unidecode
import datetime


def get_keys_from_value(d, val):
    lst = [k for k, v in d.items() if v == val]
    return lst[0]


def process_data_item_auto(item, val_brand=None, brand_id=None):
    global price
    title = item['title']
    title_normalized = unidecode(title)
    if not val_brand:
        brand = 'n/a'
        for brd in brand_list_auto:
            if brd.lower() in title.lower():
                brand = brd
                break
    else:
        brand = get_keys_from_value(brand_id, val_brand)

    params = item.get('params', [])
    for param in params:
        if param['key'] == 'price':
            if param['value']['currency'] == 'EUR':
                price = param['value']['value']
            elif param['value']['currency'] == 'RON':
                if param['value']['converted_value']:
                    price = round(float(param['value']['converted_value']))
                else:
                    price = round(float(param['value']['value'] * 0.20))
    model = next((param['value']['label'] for param in params if param['key'] == 'model'), 'n/a')
    year = next((int(param['value']['key']) for param in params if param['key'] == 'year'), 'n/a')
    enginesize = next((int(param['value']['key']) for param in params if param['key'] == 'enginesize'), 'n/a')
    km = next((int(param['value']['key']) for param in params if param['key'] == 'rulaj_pana'), 'n/a')
    state = next((param['value']['label'] for param in params if param['key'] == 'state'), 'n/a')
    petrol = next((param['value']['label'] for param in params if param['key'] == 'petrol'), 'n/a')
    car_body = next((param['value']['label'] for param in params if param['key'] == 'car_body'), 'n/a')
    color = next((param['value']['label'] for param in params if param['key'] == 'color'), 'n/a')
    door_count = next((param['value']['label'] for param in params if param['key'] == 'door_count'), 'n/a')
    gearbox = next((param['value']['label'] for param in params if param['key'] == 'gearbox'), 'n/a')
    steering_wheel = next((param['value']['label'] for param in params if param['key'] == 'steering_wheel'), 'n/a')
    created_time = item['created_time'].split('T')
    scraped_time = datetime.datetime.now().strftime("%d:%m:%y")

    return [
        brand,
        model,
        title_normalized,
        price,
        km,
        year,
        state,
        petrol,
        car_body,
        color,
        door_count,
        gearbox,
        steering_wheel,
        enginesize,
        item['url'],
        created_time[0],
        item['location']['region']['name'],
        item['location']['city']['name'] if 'city' in item['location'] else 'n/a',
        scraped_time
    ]


def process_data_item_moto(item):
    global price
    title = item['title']
    title_normalized = unidecode(title)
    brand = 'n/a'
    for brd in brand_list_moto:
        if brd.lower() in title.lower():
            brand = brd
            break

    params = item.get('params', [])
    for param in params:
        if param['key'] == 'price':
            if param['value']['currency'] == 'EUR':
                price = param['value']['value']
            elif param['value']['currency'] == 'RON':
                if param['value']['converted_value']:
                    price = round(float(param['value']['converted_value']))
                else:
                    price = round(float(param['value']['value'] * 0.20))
    year = next((int(param['value']['key']) for param in params if param['key'] == 'year'), 'n/a')
    enginesize = next((int(param['value']['key']) for param in params if param['key'] == 'enginesize'), 'n/a')
    state = next((param['value']['label'] for param in params if param['key'] == 'state'), 'n/a')
    created_time = item['created_time'].split('T')
    scraped_time = datetime.datetime.now().strftime("%d:%m:%y")

    return [
        brand,
        title_normalized,
        price,
        year,
        state,
        enginesize,
        item['url'],
        created_time[0],
        item['location']['region']['name'],
        item['location']['city']['name'] if 'city' in item['location'] else 'n/a',
        scraped_time

    ]


def unique_col_inserter(bd_path, df):
    csv_dir = f"D:/P/Webscrapers/BD/{bd_path}"
    list_of_files = glob.glob(f"{csv_dir}/*.csv")
    latest_file = max(list_of_files, key=os.path.getctime)
    prev_df = pd.read_csv(latest_file)

    if 'UniqueID' in prev_df.columns:
        last_row = prev_df.tail(1)
        highest_id = last_row['UniqueID'].values[0]
        start_index = highest_id + 1
    else:
        start_index = 1
    df.insert(0, 'UniqueID', range(start_index, start_index + len(df)))


if __name__ == '__main__':
    data = {
        "Alba": "28",
        "Arad": "1",
        "Arges": "11",
        "Bacau": "3",
        "Bihor": '19',
        "Bistrita-Nasaud": "21",
        "Botosani": '18',
        "Braila": '37',
        "Brasov": '4',
        "Bucuresti-Ilfov": '46',
        "Buzau": "36",
        "Calarasi": '40',
        "Caras-Severin": '26',
        "Cluj": '2',
        "Constanta": '7',
        "Covasna": '29',
        "Dambovita": '35',
        "Dolj": "8",
        "Galati": '9',
        "Giurgiu": '41',
        "Gorj": '33',
        "Harghita": "23",
        "Hunedoara": "27",
        "Ialomita": "39",
        "Iasi": '10',
        "Maramures": "16",
        "Mehedinti": '32',
        "Mures": '22',
        "Neamt": '24',
        "Olt": '43',
        "Prahova": "6",
        "Salaj": '20',
        "Satu Mare": '15',
        "Sibiu": '12',
        "Suceava": '17',
        "Teleorman": '42',
        "Timis": '13',
        "Tulcea": '38',
        "Valcea": '34',
        "Vaslui": '30',
        "Vrancea": '31'

    }

    print(get_keys_from_value(data, '28'))
