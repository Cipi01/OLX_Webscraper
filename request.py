import requests
from dicts import get_county_ids, get_brand_id, get_color
from funcs import get_keys_from_value

URL = "https://www.olx.ro/api/v1/offers"
region_id = get_county_ids()
region_id_list = list(region_id.values())
brand_id = get_brand_id()
brand_id_list = list(brand_id.values())
color_list = get_color()


def initial_request():
    for page in range(1, 100):
        offset = 40 * page

        querystring = {"offset": f"{offset}", "limit": "40", "category_id": "84",
                       "filter_refiners": "spell_checker",
                       "sl": "1880c28a32ex6c06d152"}

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
            "Accept": "*/*",
            "Accept-Language": "ro",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": f"https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/?page={page}",
            "X-Client": "DESKTOP",
            "X-Device-Id": "6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8",
            "X-Platform-Type": "mobile-html5",
            "Version": "v1.19",
            "X-Fingerprint": "fbdc4f53959cdb4af9c2a8983d0ffab85c6324e638a283d8d11dae88fc3236ac3fef60c9cf99daee3fef60c9cf99daeefaed307981c3a6ca4e1f7a2acddfea335a1778be62509b003fef60c9cf99daee3fef60c9cf99daee21f2c817b2cc220cb497a357830277b800d2d70001a8f455308e012c59cf7bdd93ba89d2bc096e295c6324e638a283d85a1778be62509b00e8380ebb100f22a6634c4dd7db831fb82adab689f77072074c900da77a01aaf012ef91844389788652921f5f9cea558ad4cd2dc56075a1f2d6732ea217e771924e1f7a2acddfea33e8380ebb100f22a65c6324e638a283d8faed307981c3a6ca85dd7ae142a6c1c7345bf81ff62a2ec48cd1e316ed819c76366de8f02223c248c5a848148a9a89b831b5707ea4d1cd01e0a8d9bd2152e9e07944d0618facee17bf56373776d9ec0a70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507ddf19f9ee4125e65835a462f0216186820",
            "DNT": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Authorization": "Bearer 6da3b4153438b2864b6aad54ebbe60a3a42a4797",
            "Connection": "keep-alive",
            "Cookie": "laquesis=buy-3321^@a^#buy-3422^@b^#de-1282^@a^#er-2016^@a^#er-2168^@a^#jobs-5215^@b^#jobs-5739^@b^#oesx-2887^@b^#olxeu-40669^@a^#olxeu-40670^@a^#olxeu-40896^@a^#sd-1408^@b; laquesisff=aut-388^#buy-2279^#buy-2489^#dat-2874^#decision-256^#decision-657^#do-3260^#do-3481^#euonb-114^#euweb-1372^#euweb-451^#kuna-307^#oesx-1437^#oesx-2797^#oesx-2798^#oesx-2864^#oesx-645^#oesx-867^#srt-1289^#srt-1346^#srt-1348^#srt-1434^#srt-1593^#srt-1758^#srt-684^#uacc-529^#uacc-561; lqstatus=1684771697^|1884424b31bx7ef00eea^|buy-3422^#de-1282^|^|; deviceGUID=6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8; session_start_date=1684772272207; OptanonConsent=isGpcEnabled=0&datestamp=Mon+May+22+2023+18^%^3A47^%^3A36+GMT^%^2B0300+(Eastern+European+Summer+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=ca3909aa-9920-4051-8a93-5c8ca84ebbd2&interactionCount=1&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0002^%^3A1^%^2CC0003^%^3A1^%^2CC0004^%^3A1^%^2Cgad^%^3A1^%^2CSTACK42^%^3A1&geolocation=RO^%^3BCJ&AwaitingReconsent=false; a_access_token=6da3b4153438b2864b6aad54ebbe60a3a42a4797; a_refresh_token=bfbd2140c2d8ba288208a717bb5bbb6a8cd3a694; a_grant_type=device; observed_aui=19aba8ea9b564055a9f61fc1c82e4720; user_id=675143400; user_business_status=private; onap=1880c28a32ex6c06d152-2-1884424b31bx7ef00eea-32-1684772272; OptanonAlertBoxClosed=2023-05-11T18:52:53.159Z; eupubconsent-v2=CPrpD8jPrpD8jAcABBENDECsAP_AAH_AAAYgJatf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_8glmASYatxAF2JY4E20YRQIgRhWEhVAoAKKAYWiAwgdXBTsrgJ9YRIAUAoAjAiBDgCjJgEAAAEASEQASBHggEABEAgABAAqEQgAI2AQUAFgIBAAKAaFijFAEIEhBkRERCmBARIkFBPZUIJQf6GmEIdZYAUGj_ioQESgBisCISFg5DgiQEvFkgWYo3yAEYAUAolQrUEnpoAFjIAAAAA.f_gAD_gAAAAA; OTAdditionalConsentString=1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931; dfp_user_id=c999d359-29c1-413b-b16a-04831f862ae3-ver2; _gcl_au=1.1.1749623429.1683831174; _ga_1XTP46N9VR=GS1.1.1684770436.2.1.1684770457.0.0.0; _ga=GA1.2.1432380921.1683831174; _pctx=^%^7Bu^%^7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAVg4AMAJgEA2IQE5RAgBwCA7PP4gAvkA; _pcid=^%^7B^%^22browserId^%^22^%^3A^%^22lhjhlt8wrs5cmlcw^%^22^%^7D; cX_P=lhjhlt8wrs5cmlcw; _tt_enable_cookie=1; _ttp=3EKeA_oMcNSXZvMR6Z7tq9GkxXB; _hjSessionUser_2218929=eyJpZCI6IjIzMmUxOWNmLTQyODEtNWMxNC05YmI1LTM0MjA3MGJlNjU2ZSIsImNyZWF0ZWQiOjE2ODM4MzExNzUzNDYsImV4aXN0aW5nIjp0cnVlfQ==; __gsas=ID=867bb974b017ecff:T=1683831176:S=ALNI_MatXCOxgCiabyrANBlsBSd1XSXhQA; __gads=ID=89220770a054c1f6:T=1683831176:S=ALNI_MZVNXRmoKf-h2K7-UDOWvEhdffCNw; __gpi=UID=00000bf98f05bea0:T=1683831176:RT=1684770439:S=ALNI_MZuTKVKNkt6CI7PNomtPJ6-iGcwjA; evid_0046=93268cd6-de31-4855-a11f-2c9dad4ee460; cto_bundle=jsSU8l9QSEYlMkJXZWo5VXVpNmpFQkQ5V20xaHJjZHZWSllSUmIlMkJ2akozUTUwbjU2VnY2NU0wb3BVUXExYVZ5b3lXQVByJTJCRmhlaURlVFg2SE9IZng3UXdyUVlZVktvdXJsN0lyek9BekJ5VVlPdEFtWWQzQTMlMkI1YlAyWCUyQnVIU3R6TU1HV28; ldTd=true; evid_set_0046=2; fingerprint=MTI1NzY4MzI5MTs4OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTswOzE7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MDsxOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MTswOzA7MDsxOzA7MDsxOzE7MDsxOzE7MTsxOzA7MTswOzc4NjQ4Nzc2ODsxOzI7MjsyOzI7Mjs1OzI4NDgwMDY0MTg7MTM1NzA0MTczODsxOzE7MTsxOzA7MTsxOzE7MTsxOzA7MTsxOzE7MTsxOzE7MDsxOzA7NDEwMDIxOTk7MzQ2OTMwNjU1MTszNjU2MjE2MzAxOzEzMjAxOTIyNzA7MTAwNTMwMTIwMzsxNTM2Ozg2NDsyNDsyNDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzA7MDsw; adptset_0046=1; PHPSESSID=fn0aqujr9v6gd9tvfslpqivnoc; mobile_default=desktop; laquesissu=; _gid=GA1.2.1861563183.1684770438; _gat_clientNinja=1; _hjIncludedInSessionSample_2218929=0; _hjSession_2218929=eyJpZCI6IjMxN2RlZTYxLTRjZGItNGZlNi1iNDFlLWY4NDExNDlhM2I0ZiIsImNyZWF0ZWQiOjE2ODQ3NzA0MzgxODUsImluU2FtcGxlIjpmYWxzZX0=; cX_G=cx^%^3Ax7kjdifqx1gp1lwyzl1jrljnf^%^3A3t11i2swytru7; sbjs_migrations=1418474375998^%^3D1; sbjs_current_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_first_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_current=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_first=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_udata=vst^%^3D1^%^7C^%^7C^%^7Cuip^%^3D^%^28none^%^29^%^7C^%^7C^%^7Cuag^%^3DMozilla^%^2F5.0^%^20^%^28Windows^%^20NT^%^2010.0^%^3B^%^20Win64^%^3B^%^20x64^%^3B^%^20rv^%^3A109.0^%^29^%^20Gecko^%^2F20100101^%^20Firefox^%^2F113.0; sbjs_session=pgs^%^3D5^%^7C^%^7C^%^7Ccpg^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fauto-masini-moto-ambarcatiuni^%^2Fautoturisme^%^2F^%^3Fpage^%^3D2; newrelic_cdn_name=CF; _pcus=eyJ1c2VyU2VnbWVudHMiOm51bGx9; dfp_segment=^%^5B^%^5D; newrelicInited=0",
            "TE": "trailers"
        }

        response = requests.request("GET", url=URL, data=payload, headers=headers, params=querystring)

        data_dict = response.json()
        if data_dict['metadata']['total_elements'] == 1000:
            print("NOT ALL VISIBLE")
            break


# REGIONS
def region_request():
    print("begin counties")
    for value_region1 in region_id_list:
        for page in range(1, 25):
            offset = 40 * page

            querystring = {"offset": f"{offset}", "limit": "40", "category_id": "84", "region_id": f"{value_region1}",
                           "filter_refiners": "spell_checker",
                           "sl": "1880c28a32ex6c06d152"}

            payload = ""
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
                "Accept": "*/*",
                "Accept-Language": "ro",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": f"https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/?page={page}",
                "X-Client": "DESKTOP",
                "X-Device-Id": "6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8",
                "X-Platform-Type": "mobile-html5",
                "Version": "v1.19",
                "X-Fingerprint": "fbdc4f53959cdb4af9c2a8983d0ffab85c6324e638a283d8d11dae88fc3236ac3fef60c9cf99daee3fef60c9cf99daeefaed307981c3a6ca4e1f7a2acddfea335a1778be62509b003fef60c9cf99daee3fef60c9cf99daee21f2c817b2cc220cb497a357830277b800d2d70001a8f455308e012c59cf7bdd93ba89d2bc096e295c6324e638a283d85a1778be62509b00e8380ebb100f22a6634c4dd7db831fb82adab689f77072074c900da77a01aaf012ef91844389788652921f5f9cea558ad4cd2dc56075a1f2d6732ea217e771924e1f7a2acddfea33e8380ebb100f22a65c6324e638a283d8faed307981c3a6ca85dd7ae142a6c1c7345bf81ff62a2ec48cd1e316ed819c76366de8f02223c248c5a848148a9a89b831b5707ea4d1cd01e0a8d9bd2152e9e07944d0618facee17bf56373776d9ec0a70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507ddf19f9ee4125e65835a462f0216186820",
                "DNT": "1",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Authorization": "Bearer 6da3b4153438b2864b6aad54ebbe60a3a42a4797",
                "Connection": "keep-alive",
                "Cookie": "laquesis=buy-3321^@a^#buy-3422^@b^#de-1282^@a^#er-2016^@a^#er-2168^@a^#jobs-5215^@b^#jobs-5739^@b^#oesx-2887^@b^#olxeu-40669^@a^#olxeu-40670^@a^#olxeu-40896^@a^#sd-1408^@b; laquesisff=aut-388^#buy-2279^#buy-2489^#dat-2874^#decision-256^#decision-657^#do-3260^#do-3481^#euonb-114^#euweb-1372^#euweb-451^#kuna-307^#oesx-1437^#oesx-2797^#oesx-2798^#oesx-2864^#oesx-645^#oesx-867^#srt-1289^#srt-1346^#srt-1348^#srt-1434^#srt-1593^#srt-1758^#srt-684^#uacc-529^#uacc-561; lqstatus=1684771697^|1884424b31bx7ef00eea^|buy-3422^#de-1282^|^|; deviceGUID=6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8; session_start_date=1684772272207; OptanonConsent=isGpcEnabled=0&datestamp=Mon+May+22+2023+18^%^3A47^%^3A36+GMT^%^2B0300+(Eastern+European+Summer+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=ca3909aa-9920-4051-8a93-5c8ca84ebbd2&interactionCount=1&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0002^%^3A1^%^2CC0003^%^3A1^%^2CC0004^%^3A1^%^2Cgad^%^3A1^%^2CSTACK42^%^3A1&geolocation=RO^%^3BCJ&AwaitingReconsent=false; a_access_token=6da3b4153438b2864b6aad54ebbe60a3a42a4797; a_refresh_token=bfbd2140c2d8ba288208a717bb5bbb6a8cd3a694; a_grant_type=device; observed_aui=19aba8ea9b564055a9f61fc1c82e4720; user_id=675143400; user_business_status=private; onap=1880c28a32ex6c06d152-2-1884424b31bx7ef00eea-32-1684772272; OptanonAlertBoxClosed=2023-05-11T18:52:53.159Z; eupubconsent-v2=CPrpD8jPrpD8jAcABBENDECsAP_AAH_AAAYgJatf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_8glmASYatxAF2JY4E20YRQIgRhWEhVAoAKKAYWiAwgdXBTsrgJ9YRIAUAoAjAiBDgCjJgEAAAEASEQASBHggEABEAgABAAqEQgAI2AQUAFgIBAAKAaFijFAEIEhBkRERCmBARIkFBPZUIJQf6GmEIdZYAUGj_ioQESgBisCISFg5DgiQEvFkgWYo3yAEYAUAolQrUEnpoAFjIAAAAA.f_gAD_gAAAAA; OTAdditionalConsentString=1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931; dfp_user_id=c999d359-29c1-413b-b16a-04831f862ae3-ver2; _gcl_au=1.1.1749623429.1683831174; _ga_1XTP46N9VR=GS1.1.1684770436.2.1.1684770457.0.0.0; _ga=GA1.2.1432380921.1683831174; _pctx=^%^7Bu^%^7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAVg4AMAJgEA2IQE5RAgBwCA7PP4gAvkA; _pcid=^%^7B^%^22browserId^%^22^%^3A^%^22lhjhlt8wrs5cmlcw^%^22^%^7D; cX_P=lhjhlt8wrs5cmlcw; _tt_enable_cookie=1; _ttp=3EKeA_oMcNSXZvMR6Z7tq9GkxXB; _hjSessionUser_2218929=eyJpZCI6IjIzMmUxOWNmLTQyODEtNWMxNC05YmI1LTM0MjA3MGJlNjU2ZSIsImNyZWF0ZWQiOjE2ODM4MzExNzUzNDYsImV4aXN0aW5nIjp0cnVlfQ==; __gsas=ID=867bb974b017ecff:T=1683831176:S=ALNI_MatXCOxgCiabyrANBlsBSd1XSXhQA; __gads=ID=89220770a054c1f6:T=1683831176:S=ALNI_MZVNXRmoKf-h2K7-UDOWvEhdffCNw; __gpi=UID=00000bf98f05bea0:T=1683831176:RT=1684770439:S=ALNI_MZuTKVKNkt6CI7PNomtPJ6-iGcwjA; evid_0046=93268cd6-de31-4855-a11f-2c9dad4ee460; cto_bundle=jsSU8l9QSEYlMkJXZWo5VXVpNmpFQkQ5V20xaHJjZHZWSllSUmIlMkJ2akozUTUwbjU2VnY2NU0wb3BVUXExYVZ5b3lXQVByJTJCRmhlaURlVFg2SE9IZng3UXdyUVlZVktvdXJsN0lyek9BekJ5VVlPdEFtWWQzQTMlMkI1YlAyWCUyQnVIU3R6TU1HV28; ldTd=true; evid_set_0046=2; fingerprint=MTI1NzY4MzI5MTs4OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTswOzE7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MDsxOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MTswOzA7MDsxOzA7MDsxOzE7MDsxOzE7MTsxOzA7MTswOzc4NjQ4Nzc2ODsxOzI7MjsyOzI7Mjs1OzI4NDgwMDY0MTg7MTM1NzA0MTczODsxOzE7MTsxOzA7MTsxOzE7MTsxOzA7MTsxOzE7MTsxOzE7MDsxOzA7NDEwMDIxOTk7MzQ2OTMwNjU1MTszNjU2MjE2MzAxOzEzMjAxOTIyNzA7MTAwNTMwMTIwMzsxNTM2Ozg2NDsyNDsyNDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzA7MDsw; adptset_0046=1; PHPSESSID=fn0aqujr9v6gd9tvfslpqivnoc; mobile_default=desktop; laquesissu=; _gid=GA1.2.1861563183.1684770438; _gat_clientNinja=1; _hjIncludedInSessionSample_2218929=0; _hjSession_2218929=eyJpZCI6IjMxN2RlZTYxLTRjZGItNGZlNi1iNDFlLWY4NDExNDlhM2I0ZiIsImNyZWF0ZWQiOjE2ODQ3NzA0MzgxODUsImluU2FtcGxlIjpmYWxzZX0=; cX_G=cx^%^3Ax7kjdifqx1gp1lwyzl1jrljnf^%^3A3t11i2swytru7; sbjs_migrations=1418474375998^%^3D1; sbjs_current_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_first_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_current=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_first=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_udata=vst^%^3D1^%^7C^%^7C^%^7Cuip^%^3D^%^28none^%^29^%^7C^%^7C^%^7Cuag^%^3DMozilla^%^2F5.0^%^20^%^28Windows^%^20NT^%^2010.0^%^3B^%^20Win64^%^3B^%^20x64^%^3B^%^20rv^%^3A109.0^%^29^%^20Gecko^%^2F20100101^%^20Firefox^%^2F113.0; sbjs_session=pgs^%^3D5^%^7C^%^7C^%^7Ccpg^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fauto-masini-moto-ambarcatiuni^%^2Fautoturisme^%^2F^%^3Fpage^%^3D2; newrelic_cdn_name=CF; _pcus=eyJ1c2VyU2VnbWVudHMiOm51bGx9; dfp_segment=^%^5B^%^5D; newrelicInited=0",
                "TE": "trailers"
            }

            response = requests.request("GET", url=URL, data=payload, headers=headers, params=querystring)

            data_dict_region = response.json()
            if data_dict_region['metadata']['total_elements'] == 1000:
                print(f"NOT ALL VISIBLE---{get_keys_from_value(region_id, value_region1)}")
                break
            else:
                region_id_list.remove(value_region1)
                print(f"OK---{get_keys_from_value(region_id, value_region1)}")
                break


# BRANDS
def brand_region_request():
    print("Begin brands")
    for val_region in region_id_list:
        for val_brand1 in brand_id_list:
            for page in range(1, 25):
                offset = 40 * page

                querystring = {"offset": f"0", "limit": "40", "category_id": f"{val_brand1}",
                               "region_id": f"{val_region}",
                               "filter_refiners": "spell_checker",
                               "sl": "1880c28a32ex6c06d152"}

                payload = ""
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
                    "Accept": "*/*",
                    "Accept-Language": "ro",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": f"https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/?page={page}",
                    "X-Client": "DESKTOP",
                    "X-Device-Id": "6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8",
                    "X-Platform-Type": "mobile-html5",
                    "Version": "v1.19",
                    "X-Fingerprint": "fbdc4f53959cdb4af9c2a8983d0ffab85c6324e638a283d8d11dae88fc3236ac3fef60c9cf99daee3fef60c9cf99daeefaed307981c3a6ca4e1f7a2acddfea335a1778be62509b003fef60c9cf99daee3fef60c9cf99daee21f2c817b2cc220cb497a357830277b800d2d70001a8f455308e012c59cf7bdd93ba89d2bc096e295c6324e638a283d85a1778be62509b00e8380ebb100f22a6634c4dd7db831fb82adab689f77072074c900da77a01aaf012ef91844389788652921f5f9cea558ad4cd2dc56075a1f2d6732ea217e771924e1f7a2acddfea33e8380ebb100f22a65c6324e638a283d8faed307981c3a6ca85dd7ae142a6c1c7345bf81ff62a2ec48cd1e316ed819c76366de8f02223c248c5a848148a9a89b831b5707ea4d1cd01e0a8d9bd2152e9e07944d0618facee17bf56373776d9ec0a70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507ddf19f9ee4125e65835a462f0216186820",
                    "DNT": "1",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Authorization": "Bearer 6da3b4153438b2864b6aad54ebbe60a3a42a4797",
                    "Connection": "keep-alive",
                    "Cookie": "laquesis=buy-3321^@a^#buy-3422^@b^#de-1282^@a^#er-2016^@a^#er-2168^@a^#jobs-5215^@b^#jobs-5739^@b^#oesx-2887^@b^#olxeu-40669^@a^#olxeu-40670^@a^#olxeu-40896^@a^#sd-1408^@b; laquesisff=aut-388^#buy-2279^#buy-2489^#dat-2874^#decision-256^#decision-657^#do-3260^#do-3481^#euonb-114^#euweb-1372^#euweb-451^#kuna-307^#oesx-1437^#oesx-2797^#oesx-2798^#oesx-2864^#oesx-645^#oesx-867^#srt-1289^#srt-1346^#srt-1348^#srt-1434^#srt-1593^#srt-1758^#srt-684^#uacc-529^#uacc-561; lqstatus=1684771697^|1884424b31bx7ef00eea^|buy-3422^#de-1282^|^|; deviceGUID=6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8; session_start_date=1684772272207; OptanonConsent=isGpcEnabled=0&datestamp=Mon+May+22+2023+18^%^3A47^%^3A36+GMT^%^2B0300+(Eastern+European+Summer+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=ca3909aa-9920-4051-8a93-5c8ca84ebbd2&interactionCount=1&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0002^%^3A1^%^2CC0003^%^3A1^%^2CC0004^%^3A1^%^2Cgad^%^3A1^%^2CSTACK42^%^3A1&geolocation=RO^%^3BCJ&AwaitingReconsent=false; a_access_token=6da3b4153438b2864b6aad54ebbe60a3a42a4797; a_refresh_token=bfbd2140c2d8ba288208a717bb5bbb6a8cd3a694; a_grant_type=device; observed_aui=19aba8ea9b564055a9f61fc1c82e4720; user_id=675143400; user_business_status=private; onap=1880c28a32ex6c06d152-2-1884424b31bx7ef00eea-32-1684772272; OptanonAlertBoxClosed=2023-05-11T18:52:53.159Z; eupubconsent-v2=CPrpD8jPrpD8jAcABBENDECsAP_AAH_AAAYgJatf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_8glmASYatxAF2JY4E20YRQIgRhWEhVAoAKKAYWiAwgdXBTsrgJ9YRIAUAoAjAiBDgCjJgEAAAEASEQASBHggEABEAgABAAqEQgAI2AQUAFgIBAAKAaFijFAEIEhBkRERCmBARIkFBPZUIJQf6GmEIdZYAUGj_ioQESgBisCISFg5DgiQEvFkgWYo3yAEYAUAolQrUEnpoAFjIAAAAA.f_gAD_gAAAAA; OTAdditionalConsentString=1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931; dfp_user_id=c999d359-29c1-413b-b16a-04831f862ae3-ver2; _gcl_au=1.1.1749623429.1683831174; _ga_1XTP46N9VR=GS1.1.1684770436.2.1.1684770457.0.0.0; _ga=GA1.2.1432380921.1683831174; _pctx=^%^7Bu^%^7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAVg4AMAJgEA2IQE5RAgBwCA7PP4gAvkA; _pcid=^%^7B^%^22browserId^%^22^%^3A^%^22lhjhlt8wrs5cmlcw^%^22^%^7D; cX_P=lhjhlt8wrs5cmlcw; _tt_enable_cookie=1; _ttp=3EKeA_oMcNSXZvMR6Z7tq9GkxXB; _hjSessionUser_2218929=eyJpZCI6IjIzMmUxOWNmLTQyODEtNWMxNC05YmI1LTM0MjA3MGJlNjU2ZSIsImNyZWF0ZWQiOjE2ODM4MzExNzUzNDYsImV4aXN0aW5nIjp0cnVlfQ==; __gsas=ID=867bb974b017ecff:T=1683831176:S=ALNI_MatXCOxgCiabyrANBlsBSd1XSXhQA; __gads=ID=89220770a054c1f6:T=1683831176:S=ALNI_MZVNXRmoKf-h2K7-UDOWvEhdffCNw; __gpi=UID=00000bf98f05bea0:T=1683831176:RT=1684770439:S=ALNI_MZuTKVKNkt6CI7PNomtPJ6-iGcwjA; evid_0046=93268cd6-de31-4855-a11f-2c9dad4ee460; cto_bundle=jsSU8l9QSEYlMkJXZWo5VXVpNmpFQkQ5V20xaHJjZHZWSllSUmIlMkJ2akozUTUwbjU2VnY2NU0wb3BVUXExYVZ5b3lXQVByJTJCRmhlaURlVFg2SE9IZng3UXdyUVlZVktvdXJsN0lyek9BekJ5VVlPdEFtWWQzQTMlMkI1YlAyWCUyQnVIU3R6TU1HV28; ldTd=true; evid_set_0046=2; fingerprint=MTI1NzY4MzI5MTs4OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTswOzE7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MDsxOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MTswOzA7MDsxOzA7MDsxOzE7MDsxOzE7MTsxOzA7MTswOzc4NjQ4Nzc2ODsxOzI7MjsyOzI7Mjs1OzI4NDgwMDY0MTg7MTM1NzA0MTczODsxOzE7MTsxOzA7MTsxOzE7MTsxOzA7MTsxOzE7MTsxOzE7MDsxOzA7NDEwMDIxOTk7MzQ2OTMwNjU1MTszNjU2MjE2MzAxOzEzMjAxOTIyNzA7MTAwNTMwMTIwMzsxNTM2Ozg2NDsyNDsyNDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzA7MDsw; adptset_0046=1; PHPSESSID=fn0aqujr9v6gd9tvfslpqivnoc; mobile_default=desktop; laquesissu=; _gid=GA1.2.1861563183.1684770438; _gat_clientNinja=1; _hjIncludedInSessionSample_2218929=0; _hjSession_2218929=eyJpZCI6IjMxN2RlZTYxLTRjZGItNGZlNi1iNDFlLWY4NDExNDlhM2I0ZiIsImNyZWF0ZWQiOjE2ODQ3NzA0MzgxODUsImluU2FtcGxlIjpmYWxzZX0=; cX_G=cx^%^3Ax7kjdifqx1gp1lwyzl1jrljnf^%^3A3t11i2swytru7; sbjs_migrations=1418474375998^%^3D1; sbjs_current_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_first_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_current=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_first=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_udata=vst^%^3D1^%^7C^%^7C^%^7Cuip^%^3D^%^28none^%^29^%^7C^%^7C^%^7Cuag^%^3DMozilla^%^2F5.0^%^20^%^28Windows^%^20NT^%^2010.0^%^3B^%^20Win64^%^3B^%^20x64^%^3B^%^20rv^%^3A109.0^%^29^%^20Gecko^%^2F20100101^%^20Firefox^%^2F113.0; sbjs_session=pgs^%^3D5^%^7C^%^7C^%^7Ccpg^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fauto-masini-moto-ambarcatiuni^%^2Fautoturisme^%^2F^%^3Fpage^%^3D2; newrelic_cdn_name=CF; _pcus=eyJ1c2VyU2VnbWVudHMiOm51bGx9; dfp_segment=^%^5B^%^5D; newrelicInited=0",
                    "TE": "trailers"
                }

                response = requests.request("GET", url=URL, data=payload, headers=headers, params=querystring)

                data_dict_brand = response.json()
                if data_dict_brand['metadata']['total_elements'] == 1000:
                    print(f"NOT ALL VISIBLE---{get_keys_from_value(brand_id, val_brand1)}---"
                          f"{get_keys_from_value(region_id, val_region)}")
                    break
                elif data_dict_brand['metadata']['total_elements'] == 0:
                    print(f"NO VALUE---{get_keys_from_value(brand_id, val_brand1)}---"
                          f"{get_keys_from_value(region_id, val_region)}")
                    break
                else:
                    brand_id_list.remove(val_brand1)
                    print(f"OK---{get_keys_from_value(brand_id, val_brand1)}---"
                          f"{get_keys_from_value(region_id, val_region)}")
                    break


# COLORS
def color_brand_region_request():
    print("Begin colors")
    for val_region2 in region_id_list:
        for val_brand2 in brand_id_list:
            for color in color_list:
                for page in range(1, 25):
                    offset = 40 * page

                    querystring = {"offset": f"0", "limit": "40", "category_id": f"{val_brand2}",
                                   "region_id": f"{val_region2}",
                                   'filter_enum_color^%^5B0^%^5D': f'{color}', "filter_refiners": "spell_checker",
                                   "sl": "1880c28a32ex6c06d152"}

                    payload = ""
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
                        "Accept": "*/*",
                        "Accept-Language": "ro",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Referer": f"https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/?page={page}",
                        "X-Client": "DESKTOP",
                        "X-Device-Id": "6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8",
                        "X-Platform-Type": "mobile-html5",
                        "Version": "v1.19",
                        "X-Fingerprint": "fbdc4f53959cdb4af9c2a8983d0ffab85c6324e638a283d8d11dae88fc3236ac3fef60c9cf99daee3fef60c9cf99daeefaed307981c3a6ca4e1f7a2acddfea335a1778be62509b003fef60c9cf99daee3fef60c9cf99daee21f2c817b2cc220cb497a357830277b800d2d70001a8f455308e012c59cf7bdd93ba89d2bc096e295c6324e638a283d85a1778be62509b00e8380ebb100f22a6634c4dd7db831fb82adab689f77072074c900da77a01aaf012ef91844389788652921f5f9cea558ad4cd2dc56075a1f2d6732ea217e771924e1f7a2acddfea33e8380ebb100f22a65c6324e638a283d8faed307981c3a6ca85dd7ae142a6c1c7345bf81ff62a2ec48cd1e316ed819c76366de8f02223c248c5a848148a9a89b831b5707ea4d1cd01e0a8d9bd2152e9e07944d0618facee17bf56373776d9ec0a70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507dd70926399c89507ddf19f9ee4125e65835a462f0216186820",
                        "DNT": "1",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "Authorization": "Bearer 6da3b4153438b2864b6aad54ebbe60a3a42a4797",
                        "Connection": "keep-alive",
                        "Cookie": "laquesis=buy-3321^@a^#buy-3422^@b^#de-1282^@a^#er-2016^@a^#er-2168^@a^#jobs-5215^@b^#jobs-5739^@b^#oesx-2887^@b^#olxeu-40669^@a^#olxeu-40670^@a^#olxeu-40896^@a^#sd-1408^@b; laquesisff=aut-388^#buy-2279^#buy-2489^#dat-2874^#decision-256^#decision-657^#do-3260^#do-3481^#euonb-114^#euweb-1372^#euweb-451^#kuna-307^#oesx-1437^#oesx-2797^#oesx-2798^#oesx-2864^#oesx-645^#oesx-867^#srt-1289^#srt-1346^#srt-1348^#srt-1434^#srt-1593^#srt-1758^#srt-684^#uacc-529^#uacc-561; lqstatus=1684771697^|1884424b31bx7ef00eea^|buy-3422^#de-1282^|^|; deviceGUID=6fbccf87-ca71-4b79-9bde-ac7cfa53eaa8; session_start_date=1684772272207; OptanonConsent=isGpcEnabled=0&datestamp=Mon+May+22+2023+18^%^3A47^%^3A36+GMT^%^2B0300+(Eastern+European+Summer+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=ca3909aa-9920-4051-8a93-5c8ca84ebbd2&interactionCount=1&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0002^%^3A1^%^2CC0003^%^3A1^%^2CC0004^%^3A1^%^2Cgad^%^3A1^%^2CSTACK42^%^3A1&geolocation=RO^%^3BCJ&AwaitingReconsent=false; a_access_token=6da3b4153438b2864b6aad54ebbe60a3a42a4797; a_refresh_token=bfbd2140c2d8ba288208a717bb5bbb6a8cd3a694; a_grant_type=device; observed_aui=19aba8ea9b564055a9f61fc1c82e4720; user_id=675143400; user_business_status=private; onap=1880c28a32ex6c06d152-2-1884424b31bx7ef00eea-32-1684772272; OptanonAlertBoxClosed=2023-05-11T18:52:53.159Z; eupubconsent-v2=CPrpD8jPrpD8jAcABBENDECsAP_AAH_AAAYgJatf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f__z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-f_8glmASYatxAF2JY4E20YRQIgRhWEhVAoAKKAYWiAwgdXBTsrgJ9YRIAUAoAjAiBDgCjJgEAAAEASEQASBHggEABEAgABAAqEQgAI2AQUAFgIBAAKAaFijFAEIEhBkRERCmBARIkFBPZUIJQf6GmEIdZYAUGj_ioQESgBisCISFg5DgiQEvFkgWYo3yAEYAUAolQrUEnpoAFjIAAAAA.f_gAD_gAAAAA; OTAdditionalConsentString=1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931; dfp_user_id=c999d359-29c1-413b-b16a-04831f862ae3-ver2; _gcl_au=1.1.1749623429.1683831174; _ga_1XTP46N9VR=GS1.1.1684770436.2.1.1684770457.0.0.0; _ga=GA1.2.1432380921.1683831174; _pctx=^%^7Bu^%^7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAVg4AMAJgEA2IQE5RAgBwCA7PP4gAvkA; _pcid=^%^7B^%^22browserId^%^22^%^3A^%^22lhjhlt8wrs5cmlcw^%^22^%^7D; cX_P=lhjhlt8wrs5cmlcw; _tt_enable_cookie=1; _ttp=3EKeA_oMcNSXZvMR6Z7tq9GkxXB; _hjSessionUser_2218929=eyJpZCI6IjIzMmUxOWNmLTQyODEtNWMxNC05YmI1LTM0MjA3MGJlNjU2ZSIsImNyZWF0ZWQiOjE2ODM4MzExNzUzNDYsImV4aXN0aW5nIjp0cnVlfQ==; __gsas=ID=867bb974b017ecff:T=1683831176:S=ALNI_MatXCOxgCiabyrANBlsBSd1XSXhQA; __gads=ID=89220770a054c1f6:T=1683831176:S=ALNI_MZVNXRmoKf-h2K7-UDOWvEhdffCNw; __gpi=UID=00000bf98f05bea0:T=1683831176:RT=1684770439:S=ALNI_MZuTKVKNkt6CI7PNomtPJ6-iGcwjA; evid_0046=93268cd6-de31-4855-a11f-2c9dad4ee460; cto_bundle=jsSU8l9QSEYlMkJXZWo5VXVpNmpFQkQ5V20xaHJjZHZWSllSUmIlMkJ2akozUTUwbjU2VnY2NU0wb3BVUXExYVZ5b3lXQVByJTJCRmhlaURlVFg2SE9IZng3UXdyUVlZVktvdXJsN0lyek9BekJ5VVlPdEFtWWQzQTMlMkI1YlAyWCUyQnVIU3R6TU1HV28; ldTd=true; evid_set_0046=2; fingerprint=MTI1NzY4MzI5MTs4OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTswOzE7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MDsxOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MTswOzA7MDsxOzA7MDsxOzE7MDsxOzE7MTsxOzA7MTswOzc4NjQ4Nzc2ODsxOzI7MjsyOzI7Mjs1OzI4NDgwMDY0MTg7MTM1NzA0MTczODsxOzE7MTsxOzA7MTsxOzE7MTsxOzA7MTsxOzE7MTsxOzE7MDsxOzA7NDEwMDIxOTk7MzQ2OTMwNjU1MTszNjU2MjE2MzAxOzEzMjAxOTIyNzA7MTAwNTMwMTIwMzsxNTM2Ozg2NDsyNDsyNDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzA7MDsw; adptset_0046=1; PHPSESSID=fn0aqujr9v6gd9tvfslpqivnoc; mobile_default=desktop; laquesissu=; _gid=GA1.2.1861563183.1684770438; _gat_clientNinja=1; _hjIncludedInSessionSample_2218929=0; _hjSession_2218929=eyJpZCI6IjMxN2RlZTYxLTRjZGItNGZlNi1iNDFlLWY4NDExNDlhM2I0ZiIsImNyZWF0ZWQiOjE2ODQ3NzA0MzgxODUsImluU2FtcGxlIjpmYWxzZX0=; cX_G=cx^%^3Ax7kjdifqx1gp1lwyzl1jrljnf^%^3A3t11i2swytru7; sbjs_migrations=1418474375998^%^3D1; sbjs_current_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_first_add=fd^%^3D2023-05-22^%^2018^%^3A47^%^3A20^%^7C^%^7C^%^7Cep^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fd^%^2Foferta^%^2Fperne-de-aer-renault-sprinter-peugeot-crafter-citroen-opel-iveco-lt-IDbpD9l.html^%^7C^%^7C^%^7Crf^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2F; sbjs_current=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_first=typ^%^3Dtypein^%^7C^%^7C^%^7Csrc^%^3D^%^28direct^%^29^%^7C^%^7C^%^7Cmdm^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccmp^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ccnt^%^3D^%^28none^%^29^%^7C^%^7C^%^7Ctrm^%^3D^%^28none^%^29; sbjs_udata=vst^%^3D1^%^7C^%^7C^%^7Cuip^%^3D^%^28none^%^29^%^7C^%^7C^%^7Cuag^%^3DMozilla^%^2F5.0^%^20^%^28Windows^%^20NT^%^2010.0^%^3B^%^20Win64^%^3B^%^20x64^%^3B^%^20rv^%^3A109.0^%^29^%^20Gecko^%^2F20100101^%^20Firefox^%^2F113.0; sbjs_session=pgs^%^3D5^%^7C^%^7C^%^7Ccpg^%^3Dhttps^%^3A^%^2F^%^2Fwww.olx.ro^%^2Fauto-masini-moto-ambarcatiuni^%^2Fautoturisme^%^2F^%^3Fpage^%^3D2; newrelic_cdn_name=CF; _pcus=eyJ1c2VyU2VnbWVudHMiOm51bGx9; dfp_segment=^%^5B^%^5D; newrelicInited=0",
                        "TE": "trailers"
                    }

                    response = requests.request("GET", url=URL, data=payload, headers=headers, params=querystring)

                    data_dict_brand = response.json()
                    if data_dict_brand['metadata']['total_elements'] == 1000:
                        print("NOT ALL VISIBLE")
                        break
                    else:
                        color_list.remove(color)
                        print("OK")
                        break

if __name__ == '__main__':
    brand_region_request()
