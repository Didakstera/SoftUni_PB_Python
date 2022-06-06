pack_pens = 5.80
pack_markers = 7.20
litre_detergent = 1.20
pack_pens_amount = int(input())
pack_markers_amount = int(input())
litres_detergent_amount = int(input())
discount = int(input())
pens_price = pack_pens * pack_pens_amount
markers_price = pack_markers * pack_markers_amount
detergent_price = litre_detergent * litres_detergent_amount
price_without_discount = pens_price + markers_price + detergent_price
price_with_discount = price_without_discount - price_without_discount * discount / 100
print(price_with_discount)
