world_record = float(input())
distance_in_meters = float(input())
seconds_in_a_meter = float(input())
water_resistance = distance_in_meters // 15
water_resistance_slowing = water_resistance * 12.5
ivancho_record = ((distance_in_meters * seconds_in_a_meter) + water_resistance_slowing)
if ivancho_record < world_record:
    print(f"Yes, he succeeded! The new world record is {ivancho_record:.2f} seconds.")
if ivancho_record >= world_record:
    print(f"No, he failed! He was {(ivancho_record - world_record):.2f} seconds slower.")
