from collections import namedtuple
import numpy as np
input_file ="sample.txt" if 0 else "input.txt"

def rotate(beacon, axis):
    r_coords = beacon[:axis] + beacon[axis+1:]
    res = [
        [ r_coords[0],  r_coords[1]],
        [-r_coords[1],  r_coords[0]],
        [-r_coords[0], -r_coords[1]],
        [ r_coords[1], -r_coords[0]]
    ]
    return [r[:axis] + [beacon[axis]] + r[axis:] for r in res]

def rotations(beacon):
    return \
        rotate([ beacon[0],  beacon[1],  beacon[2]], axis=1) +\
        rotate([ beacon[1], -beacon[0],  beacon[2]], axis=0) +\
        rotate([-beacon[0], -beacon[1],  beacon[2]], axis=1) +\
        rotate([-beacon[1],  beacon[0],  beacon[2]], axis=0) +\
        rotate([ beacon[0],  beacon[2], -beacon[1]], axis=2) +\
        rotate([ beacon[0], -beacon[2],  beacon[1]], axis=2)

def scanner_rotations(scanner_beacons):
    return np.array([list(x) for x in zip(*[rotations(beacon) for beacon in scanner_beacons])])

def overlap(scanner_1, scanner_2):
    s_1_b = {tuple(beacon) for beacon in scanner_1.beacons}
    for rotated_beacons in scanner_rotations(scanner_2.beacons):
        for scanner_2_beacon in rotated_beacons:
            for scanner_1_beacon in scanner_1.beacons:
                shift = scanner_1_beacon - scanner_2_beacon
                # NOTE: readable version of the if below:
                # hits = 0
                # for unshifted_scanner_2_beacon in rotated_beacons:
                #     if any((scanner_1.beacons[:]==(unshifted_scanner_2_beacon + shift)).all(1)):
                #         hits += 1
                if len({tuple(beacon) for beacon in rotated_beacons+shift}.intersection(s_1_b)) >= 12:
                    return True, shift, rotated_beacons + shift
    return False, None, None

with open(input_file) as inp:
    scanners = [namedtuple("Scanner", "coords beacons")(
        np.zeros(3, dtype=int),
        np.array([list(map(int, beacon.split(','))) for beacon in beacons.split('\n')[1:-2]])
        ) for beacons in inp.read().split("---")[2::2]
    ]

    are_all_scanners = [0]
    tested = set([(i, i) for i in range(len(scanners))])
    all_beacons = set([tuple(beacon) for beacon in scanners[0].beacons])
    reconstructed = [(0, scanners[0])]
    while len(are_all_scanners) < len(scanners):
        # NOTE: Progress output
        print(len(reconstructed))
        for index_scanner_2 in range(len(scanners)):
            intersect = False
            for orig_index_s_1, scanner_1 in reconstructed:
                if (orig_index_s_1, index_scanner_2) in tested:
                    continue
                if (index_scanner_2, orig_index_s_1) in tested:
                    continue
                tested.update([(orig_index_s_1, index_scanner_2)])
                intersect, new_coords, new_beacons_coords = \
                				overlap(scanner_1, scanners[index_scanner_2])
                if intersect:
                    # NOTE: Progress output
                    print(scanners[index_scanner_2].beacons[0])
                    are_all_scanners.append(index_scanner_2)
                    all_beacons.update(set([tuple(beacon) for beacon in new_beacons_coords]))
                    reconstructed.append(
                      (
                        index_scanner_2,
                        namedtuple("Scanner", "coords beacons")(new_coords, new_beacons_coords)
                      )
                    )
                    break
    print(len(all_beacons))

    def dst(a,b):
        return np.sum(np.abs(a - b))

    maxim = 0
    tmp = [scanner.coords for _, scanner in reconstructed]
    for a in range(len(tmp)):
        for b in range(a+1, len(tmp)):
            maxim = max(maxim, dst(tmp[a],tmp[b]))
    print(maxim)
