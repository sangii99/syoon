move_count = 0
count_A, count_B, count_C = 0, 0, 0
def hanoi(n):
    if n == 1: # solve for n = 1
        count_A -= 1
        count_C += 1
        move_count += 1
        print(f"Disc {n} from A to C")
        print(f"{move_count} moves needed")
    else: # solve for n-1
        if count_B == 0 and count_C == 0:
            print(f"Disc {n-(n-1)} from A to B")
            count_A -= 1
            count_B += 1
            move_count += 1
            hanoi(n-1)
        elif count_B != 0 and count_C == 0:
            print(f"Disc {n-(n-1)} from A to C")
            count_A -= 1
            count_C += 1
            move_count += 1
            hanoi(n-1)
        elif count_B != 0 and count_C != 0:
            print(f"Disc {n-(n-1)} from C to A")
            count_C -= 1
            count_A += 1
            move_count += 1
            hanoi(n-1)
        return hanoi(n-1)