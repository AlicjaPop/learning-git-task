shops_dict = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista Zakupów")

product_list=[]
for shop, product in shops_dict.items():
    Shop=shop.capitalize()
    print(f"Idę do {Shop}, kupuję tu następujące rzeczy:", shops_dict[shop])
    product_list=product_list + shops_dict[shop]
print(f"W sumie kupuję", len(product_list), "produktów.")