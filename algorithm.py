class Disk:
    def __init__(self, x, y):
        self.x = x
        self.y = y

UNIT_LENGTH = 18

current_state = {
    "grid_coordinate": None,
    "current_packing": [],
    "fully_contained": [],
    "currently_checking": [],
    "current_best": [],
}

def cleanup(disks, k, offset):
    fully_contained = []
    disks_in_grid = []

    for disk in disks:
        local_x = (disk.x - offset[0]) % (UNIT_LENGTH*k)
        local_y = (disk.y - offset[1]) % (UNIT_LENGTH*k)

        if local_x < UNIT_LENGTH or local_x > UNIT_LENGTH*k - UNIT_LENGTH or local_y < UNIT_LENGTH or local_y > UNIT_LENGTH*k - UNIT_LENGTH:
            disks_in_grid.append(disk)
            continue

        fully_contained.append(disk)

    return fully_contained, disks_in_grid


def can_add(disk, currently_checking, disks):
    for i in currently_checking:
        if (disk.x - disks[i].x)**2 + (disk.y - disks[i].y)**2 < (2*UNIT_LENGTH)**2:
            return False
    return True

def packing_local(disks, k, currently_checking):
    global current_state
    if len(currently_checking) > k**2:
        return
    
    current_state["currently_checking"] = [disks[i] for i in currently_checking]
    if len(currently_checking) > len(current_state["current_best"]):
        current_state["current_best"] = [disks[i] for i in currently_checking]
    
    yield current_state

    begin = 0
    if len(currently_checking) > 0:
        begin = currently_checking[-1] + 1

    for i in range(begin, len(disks)):
        if can_add(disks[i], currently_checking, disks):
            yield from packing_local(disks, k, currently_checking + [i])

def packing(disks, k, offset):
    global current_state

    for cx in range(offset[0] - UNIT_LENGTH*k, 1200, UNIT_LENGTH*k):
        for cy in range(offset[1] - UNIT_LENGTH*k, 560, UNIT_LENGTH*k):
            print(cx, cy)

            current_state["grid_coordinate"] = (cx, cy)

            fully_contained = []
            for disk in disks:
                if cx <= disk.x < cx + UNIT_LENGTH*k and cy <= disk.y < cy + UNIT_LENGTH*k:
                    fully_contained.append(disk)
            
            current_state["fully_contained"] = fully_contained

            print(current_state)

            yield from packing_local(fully_contained, k, [])

            current_state["current_packing"] += current_state["current_best"]
            current_state["current_best"] = []


if __name__ == "__main__":
    offset = (20, 30)
    k = 10
    disks = [Disk(50, 50), Disk(60, 60)]

    active_disks, disks_in_grid = cleanup(disks, k, offset)
    gen = packing(active_disks, k, offset)
    for state in gen:
        print(state)

    pass