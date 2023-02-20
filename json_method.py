import requests
import json
from headers import headers


# def get_json():
#     for i in range(1, 101):
#         url = f"https://catalog.wb.ru/catalog/bl_shirts/catalog?cat=8126&limit=100&sort=popular&page={i}&appType=128&curr=byn&locale=by&lang=ru&dest=12358386,12358404,3,-59208&regions=1,4,22,30,31,33,40,48,66,68,69,70,80,83&emp=0&reg=1&pricemarginCoeff=1.0&offlineBonus=0&onlineBonus=0&spp=25"
#
#         try:
#             req = requests.get(url=url, headers=headers).json()
#
#             with open(f"data/{i}_page.json", "w", encoding="utf-8") as file:
#                 json.dump(req, file, indent=4, ensure_ascii=False)
#                 file.close()
#         except Exception as ex:
#             with open(f"data/{i}_page.json", "w", encoding="utf-8") as file:
#                 file.write(f"page not found\n{i}\n{url}")
#                 file.close()

        # break

products_info = []

def get_info_result():
    for i in range(1, 101):
        with open(f"data/{i}_page.json", encoding="utf-8") as file:
            json_dict = json.load(file)

            products_list = json_dict["data"]["products"]

            inner_i = 1
            for product in products_list:
                id = product["id"]
                link = f"https://www.wildberries.by/product?card={id}&category=8126"
                name = product["name"]
                start_price = product["priceU"]
                sale_price = product["salePriceU"]
                color = product["colors"][0]["name"]

                sizes_list = []
                size = product["sizes"]
                for item_size in size:
                    origin_size = item_size["origName"]
                    name_size = item_size["name"]

                    sizes_list.append(
                        {
                            origin_size: name_size,
                        }
                    )

                products_info.append(
                    {
                        "number": inner_i,
                        "title": name,
                        "start_price": start_price,
                        "sale_price": sale_price,
                        "color": color,
                        "link": link,
                        "sizes": sizes_list
                    }
                )

                inner_i += 1
        i += 1
        break
    return products_info


with open("result_info.json", "w", encoding="utf-8") as file:
    json.dump(get_info_result(), file, indent=4, ensure_ascii=False)

# get_json()

