from funcs import unique_col_inserter
from OLX_MOTO.request import region_req, region_eng_req
from OLX_AUTO.request import initial_request, direct_brand_request, region_request, brand_region_request, \
    color_brand_region_request, chassis_color_brand_region_request
from dicts import columns_moto, columns_auto
import pandas as pd
from datetime import datetime

DATE = datetime.now().strftime("%d_%m_%y")


def run_moto():
    region_plus_list, data_list = region_req()
    data_list = region_eng_req(region_plus_list, data_list)
    df = pd.DataFrame(data_list, columns=columns_moto)
    df = df.drop_duplicates()
    unique_col_inserter("OLX_MOTO", df)
    df.to_csv(f"D:/P/Webscrapers/BD/OLX_MOTO/OLX_MOTO_{DATE}.csv", index=False)


def run_auto():
    data_list = initial_request()
    brand_list_rmn1, data_list, brand_s_dict = direct_brand_request(data_list)
    reg_plus_list, data_list = region_request(data_list)
    brd_reg_plus_dict, data_list = brand_region_request(data_list, reg_plus_list, brand_list_rmn1)
    cbr_brd_rmn, cbr_color_rmn, data_list = color_brand_region_request(data_list)
    data_list = chassis_color_brand_region_request(data_list, cbr_color_rmn)
    df = pd.DataFrame(data_list, columns=columns_auto)
    df = df.drop_duplicates()
    unique_col_inserter("OLX_AUTO", df)
    df.to_csv(f"D:/P/Webscrapers/BD/OLX_AUTO/OLX_AUTO_{DATE}.csv", index=False)
