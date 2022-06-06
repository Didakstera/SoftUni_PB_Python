groups_trekkers = int(input())
peak = ""
musala_trekkers = 0
mont_blanc_trekkers = 0
kilimanjaro_trekkers = 0
k2_trekkers = 0
everest_trekkers = 0
for groups in range(1, groups_trekkers + 1):
    amount_people_in_group = int(input())
    if amount_people_in_group <= 5:
        musala_trekkers += amount_people_in_group
        peak = "Musala"
    elif 6 <= amount_people_in_group <= 12:
        mont_blanc_trekkers += amount_people_in_group
        peak = "Mont Blanc"
    elif 13 <= amount_people_in_group <= 25:
        kilimanjaro_trekkers += amount_people_in_group
        peak = "Kilimanjaro"
    elif 26 <= amount_people_in_group <= 40:
        k2_trekkers += amount_people_in_group
        peak = "K2"
    elif 41 <= amount_people_in_group:
        everest_trekkers += amount_people_in_group
        peak = "Everest"
all_people = musala_trekkers + mont_blanc_trekkers + kilimanjaro_trekkers + k2_trekkers + everest_trekkers
musala_percents = musala_trekkers / all_people * 100
mont_blanc_percents = mont_blanc_trekkers / all_people * 100
kilimanjaro_percents = kilimanjaro_trekkers / all_people * 100
k2_percents = k2_trekkers / all_people * 100
everest_percents = everest_trekkers / all_people * 100
print(f"{musala_percents:.2f}%")
print(f"{mont_blanc_percents:.2f}%")
print(f"{kilimanjaro_percents:.2f}%")
print(f"{k2_percents:.2f}%")
print(f"{everest_percents:.2f}%")
