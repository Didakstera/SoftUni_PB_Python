packing_paper_amount = int(input())
cloth_rolls_amount = int(input())
glue_litres_amount = float(input())
discount_percent = int(input())
single_roll_paper = 5.80
single_roll_cloth = 7.20
one_litre_glue = 1.20
price_for_paper = packing_paper_amount * single_roll_paper
price_for_cloth = cloth_rolls_amount * single_roll_cloth
price_for_glue = glue_litres_amount * one_litre_glue
needed_sum_before_discount = price_for_paper + price_for_cloth + price_for_glue
needed_sum_final = needed_sum_before_discount - needed_sum_before_discount * discount_percent / 100
print(f"{needed_sum_final:.3f}")
