def main():
    n = int(input('Enter the number of disks: '))
    hanoi(n)
    #moveDisks(n, 'A', 'B', 'C')

def hanoi(n):
    fromTower = 'A'
    toTower = 'C'
    auxTower = 'B'
    moveDisks(n, fromTower, toTower, auxTower)
    print((2**n - 1), "moves needed")


def moveDisks(n, fromTower, toTower, auxTower):
    '''
    fromTower = tower that the disks are initially in (tower A)
    toTower = tower that we want to move the disks to (tower C)
    auxTower = auxiliary tower, for assistance (tower B)

    n = 1 >> move disk 1 from fromtower to totower
    n > 1 >> moveDisks(n - 1, fromTower, auxTower, toTower)
    move disk n from fromtower to totower
    moveDisks(n - 1, auxTower, toTower, fromTower)
    '''
    if n == 1:
        print("Disc", n, 'from', fromTower, 'to', toTower)
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Disc", n, 'from', fromTower, 'to', toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower)

main()

#print((2 ^ n - 1), "moves needed")