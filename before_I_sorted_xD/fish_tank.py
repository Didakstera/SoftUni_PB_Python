height = int(input())
width = int(input())
length = int(input())
accessories = float(input())
aquarium_volume_in_cm = height * width * length
aquarium_volume_in_dm = aquarium_volume_in_cm / 1000
needed_litres = aquarium_volume_in_dm - aquarium_volume_in_dm * accessories / 100
print(needed_litres)
