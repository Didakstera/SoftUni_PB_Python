chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery_fee = 2.50
chick_menu_amount = int(input())
fish_menu_amount = int(input())
vegan_menu_amount = int(input())
chick_menus_price = chick_menu_amount * chicken_menu
fish_menus_price = fish_menu * fish_menu_amount
vegan_menus_price = vegan_menu_amount * vegan_menu
all_menus_price = chick_menus_price + fish_menus_price + vegan_menus_price
deserts_price = all_menus_price * 0.2
total_price = all_menus_price + deserts_price + delivery_fee
print(total_price)


