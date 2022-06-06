petar_budget = float(input())
video_cards_amount = int(input())
processors_amount = int(input())
ram_memories_amount = int(input())
video_card_price = 250
all_video_cards_price = 250 * video_cards_amount
processor_price = all_video_cards_price * 0.35
ram_memory_price = all_video_cards_price * 0.10
all_processors_price = processor_price * processors_amount
all_ram_memories_price = ram_memory_price * ram_memories_amount
all_tech_cost = all_video_cards_price + all_processors_price + all_ram_memories_price
if video_cards_amount > processors_amount:
    all_tech_cost = all_tech_cost - all_tech_cost * 0.15
if all_tech_cost <= petar_budget:
    print(f"You have {(petar_budget - all_tech_cost):.2f} leva left!")
else:
    print(f"Not enough money! You need {(all_tech_cost - petar_budget):.2f} leva more!")
