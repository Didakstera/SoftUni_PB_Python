cake_length = int(input())
cake_width = int(input())
cake_area = cake_length * cake_width
all_pieces = cake_area
single_take = ""
pieces_taken = 0
while all_pieces > pieces_taken:
    single_take = input()
    if single_take == "STOP":
        break
    else:
        pieces_taken += int(single_take)
if single_take == "STOP":
    print(f"{all_pieces - pieces_taken} pieces are left.")
elif pieces_taken > all_pieces:
    print(f"No more cake left! You need {pieces_taken - all_pieces} pieces more.")
