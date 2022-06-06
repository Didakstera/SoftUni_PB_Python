dog_food_price_per_pack = 2.5
cat_food_price_per_pack = 4
total_packs_dog = int(input())
total_packs_cat = int(input())
total_price = dog_food_price_per_pack * total_packs_dog + cat_food_price_per_pack * total_packs_cat
print(f"{total_price} lv.")