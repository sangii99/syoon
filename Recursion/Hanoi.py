def hanoi(n): # n = number of disks
    count_A, count_B, count_C = n, 0, 0
    move_count = 0
    if n == 1:
        count_A -= 1
        count_C += 1
        move_count += 1
        return(f"move disc {n} from pole A to pole C")

    elif n > 1 and count_A == n and count_B == 0 and count_C == 0: # solve using C as temporary for B
        print(f"move disc {n-(n-1)} from pole A to pole B")
        move_count += 1
        count_A -= 1
        count_B += 1
        print(f"move disc {n-(n-2)} from pole A to pole C")
        move_count += 1
        count_C += 1
        count_A -= 1
        print(f"move disc {n-(n-1)} from pole B to pole C")
        move_count += 1
        count_C += 1
        count_B -= 1
    elif n > 1 and (0 < count_A < n) and count_B != 0 and count_C == 0:
        print(f"move disc {n} from pole A to pole B")
        count_A -= 1
        count_B += 1
        move_count += 1
        print(f"move disc {n-(n-1)} from pole C to pole A")
        move_count += 1
        count_C -= 1
        count_A += 1
        print(f"move disc {n-(n-2)} from pole C to pole B")
        move_count += 1
        count_B += 1
        count_C -= 1
    elif n > 1 and (0 < count_A < n) and count_C == 0:
        print(f"move disc {n} from pole A to pole C")
        count_A -= 1
        count_C += 1
        move_count += 1
        return hanoi(n-1)