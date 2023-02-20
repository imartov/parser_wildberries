import json
import requests
from headers import headers


url = "https://catalog.wb.ru/menu/v7/api?lang=ru&locale=by&country=by&location=sng"

def get_categories():
    rec = requests.get(url=url, headers=headers).json()

    with open("site_categories.json", "w", encoding="utf-8") as file:
        json.dump(rec, file, indent=4, ensure_ascii=False)
        file.close()

    with open("site_categories.json", encoding="utf-8") as file:
        data_cat = json.load(file)

    cats = []
    for one_type_item in data_cat["data"]:                                  # женщинам, детям, мужчинам
        if "nodes" in one_type_item:
            two_type_list = []
            for two_type_item in one_type_item["nodes"]:                    # блузки, рубашки
                if "nodes" in two_type_item:
                    tree_type_list = []
                    for tree_type_item in two_type_item["nodes"]:           # аксессуры
                        tree_type_list.append(
                            {
                                tree_type_item["name"]: tree_type_item["id"],
                                "link_key": tree_type_item["shardKey"]
                            }
                        )
                    two_type_list.append(
                        {
                            two_type_item["name"]: two_type_item["id"],
                            "link_key": two_type_item["shardKey"],
                            "nodes": tree_type_list
                        }
                    )
                else:
                    two_type_list.append(
                        {
                            two_type_item["name"]: two_type_item["id"],
                            "link_key": two_type_item["shardKey"],
                        }
                    )
            cats.append(
                {
                    one_type_item["name"]: one_type_item["id"],
                    "link_key": one_type_item["shardKey"],
                    "nodes": two_type_list
                }
            )
        else:
            cats.append(
                {
                    one_type_item["name"]: one_type_item["id"],
                    "link_key": one_type_item["shardKey"],
                }
            )

    with open("result_cats.json", "w", encoding="utf-8") as file:
        json.dump(cats, file, indent=4, ensure_ascii=False)
        file.close()


get_categories()