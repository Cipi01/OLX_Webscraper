def get_county_ids():
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
    return data


def get_brand_id():
    data = {
        "Abarth": "2533",
        "Acura": '2534',
        "Aixam": '772',
        "Alfa-Romeo": '181',
        "Aro": '2535',
        "Aston-Martin": '2536',
        "Audi": '182',
        "Bentley": '2539',
        "BMW": '183',
        "Buick": '2541',
        "Cadillac": '841',
        "Chevrolet": '184',
        "Chrysler": '185',
        "Citroen": '186',
        "Comarth": '2542',
        "Dacia": '742',
        "Daewoo": '187',
        "Daihatsu": '837',
        "Dodge": '770',
        "Ferarri": '2543',
        "Fiat": '188',
        "Ford": '189',
        "GMC": '2545',
        "Honda": '190',
        "Hummer": '827',
        "Hyundai": '191',
        "Infiniti": '831',
        "Isuzu": '835',
        "Jaguar": '769',
        "Jeep": '768',
        "Kia": '192',
        "Lada": '771',
        "Lamborghini": '2546',
        "Lancia": '193',
        "Land Rover": '762',
        "Lexus": '767',
        "Ligier": '2547',
        "Lincoln": '2548',
        "Maserati": '2550',
        "Maybach": '2551',
        "Mazda": '194',
        "McLaren": '2552',
        "Mercedes-Benz": '195',
        "MG": '825',
        "Mini": '2554',
        "Mitshbishi": '196',
        "Microcar": '2553',
        "Nissan": '197',
        "Opel": '198',
        "Peuget": '199',
        "Pontiac": '833',
        "Porsche": '829',
        "Renault": '200',
        "Rolls-Royce": '2556',
        "Rover": '296',
        "Saab": '201',
        "Seat": '202',
        "Skoda": '203',
        "Smart": '760',
        "SsangYong": '823',
        "Skywell": '2557',
        "Subaru": '204',
        "Suzuki": '205',
        "Tesla": '1638',
        "Tata": '2558',
        "Tazari": '2559',
        "Toyota": '206',
        "Trabant": '2560',
        "Volkswagen": '207',
        "Volvo": '208',
        "Alte marci": '209'
    }
    return data


def get_color():
    data = ['white', 'black', 'gray', 'silver', 'blue', 'red', 'green', 'gold', 'beige', 'other']
    return data


def get_chassis():
    data = ['cabriolet', 'sedan', 'coupe', 'suv', 'hatchback', 'estate-car', 'off-road-vehicle', 'mvp']
    return data


if __name__ == '__main__':
    data1 = get_county_ids()
    for values in data1.values():
        print(values)
