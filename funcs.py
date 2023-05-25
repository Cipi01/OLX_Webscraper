def get_keys_from_value(d, val):
    lst = [k for k, v in d.items() if v == val]
    return lst[0]
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

    print(get_keys_from_value(data,'28'))