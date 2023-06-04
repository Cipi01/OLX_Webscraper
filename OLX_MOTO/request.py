import requests
from dicts import region_dict
from funcs import get_keys_from_value, process_data_item_moto


def region_req():
    data_list = []
    region_plus_list = []
    region_id_list = list(region_dict.values())
    for val_region in region_id_list:
        for page in range(1, 25):
            if page == 1:
                offset = 0
            else:
                offset += 40
            url = f"https://www.olx.ro/api/v1/offers/?limit=40&category_id=1045&currency=EUR&" \
                  f"&page={page}&filter_refiners=spell_checker&" \
                  f"sl=18844452377x208b1b88&offset={offset}&region_id={val_region}"

            payload = {}
            headers = {
                'Cookie': 'PHPSESSID=8r8vl4c4rpe5ii2akj71kndu77'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            data = response.json()
            try:
                if data['metadata']['total_elements'] == 1000:
                    region_plus_list.append(val_region)
                    break
                elif data['metadata']['total_elements'] == 0:
                    break
                else:
                    if not data['data']:

                        break
                    for i in data['data']:
                        data_list.append(process_data_item_moto(i))
            except IndexError or KeyError:
                break
    return region_plus_list, data_list


def region_eng_req(region_plus_list, data_list):
    for val_region in region_plus_list:
        for val_eng1, val_eng2 in zip(['0', '600'], ['600', '10000']):
            for page in range(1, 25):
                if page == 1:
                    offset = 0
                else:
                    offset += 40
                url = f"https://www.olx.ro/api/v1/offers/?offset={offset}&limit=40&category_id=1045&" \
                      f"region_id={val_region}&currency=EUR&page={page}" \
                      f"&filter_enum_state%5B0%5D=used&filter_float_enginesize%3Afrom={val_eng1}&" \
                      f"filter_float_enginesize%3Ato={val_eng2}&filter_refiners=spell_checker&sl=18844452377x208b1b88"
                payload = {}
                headers = {
                    'Cookie': 'PHPSESSID=8r8vl4c4rpe5ii2akj71kndu77'
                }

                response = requests.request("GET", url, headers=headers, data=payload)

                data = response.json()
                try:
                    if data['metadata']['total_elements'] == 1000:
                        break
                    elif data['metadata']['total_elements'] == 0:
                        break
                    else:
                        if not data['data']:
                            break
                        for i in data['data']:
                            data_list.append(process_data_item_moto(i))
                except IndexError or KeyError:
                    break
    return data_list

if __name__ == '__main__':
    region_req()