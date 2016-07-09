# Solve N persons crossing a bridge problem
# Two persons can cross at a time sharing one torch. One person has to
# return with the torch. The N persons cross the bridge at different speeds.
# When a pair cross the bridge, their speed is determined by the slowest of
# them. The objective of the puzzle is to find the combination of persons
# going back and forth until all N persons are on the other side in the
# least possible amount of time.

# Author: D. Murali

import sys
import itertools

# The set of people at the origin of the bridge
#source = [ 'A', 'B', 'C', 'D' ]
source = []

# Time to cross the bridge for each person
#crossing_time = { 'A':1, 'B':2, 'C':7, 'D':10 }
crossing_time = {}

# The set of people on the other side of the bridge
dest = []

# Move a person with the torch from destination to source
def move_single(source, dest, l, time_taken, level, solution, solution_set):
    dest.remove(l)
    source.append(l)
    #print '    Moving (', l , ')', ': ', source, dest,
    #print ' Cost: ', crossing_time[l]
    time_taken += crossing_time[l]
    solution += ', ' + str(l) + ', '
    solve(source[:], dest[:], time_taken, level+1, solution, solution_set)

# Move a pair of persons from source to destination
def move_pair(source, dest, node, time_taken, level, solution, solution_set):
    if len(source) == 0:
        return

    x = node[0]
    y = node[1]
    #print 'Moving: ', x, y, ' source: ', source,
    #print ' dest: ', dest
    source.remove(x)
    source.remove(y)
    dest.append(x)
    dest.append(y)
    time_taken += max(crossing_time[x], crossing_time[y])
    #print 'Moving (', x, ',', y, ')', ' to dest: ', source, dest,
    solution += str(x) + '+' + str(y)
    #print ' Cost: ', max(crossing_time[x], crossing_time[y])

    # All persons crossed over?
    if len(source) == 0:
        #print 'Solution: (', solution, ')',
        #print ' Total Time: ', time_taken, 'min'
        #print '---------------------------------------------------'
        solution_set.append((solution, time_taken))
        return

    for l in dest:
        #print 'source: ', source, ' dest: ', dest
        move_single(source[:], dest[:], l, time_taken, level, solution, solution_set)


def solve(source, dest, time_taken, level, solution, solution_set):

    #print 'solve: level', level, ' source: ', source, ' dest: ', dest

    if len(source) == 0:
        return

    comb = itertools.combinations(source, 2)

    ct = []

    # loop over all possible combinations of pairs
    for x, y in comb:
        ct.append((x, y))

    #print 'combinations: ', ct

    for node in ct:
        move_pair(source[:], dest[:], node, time_taken, level, solution, solution_set)

solution_set = []

# Handle 0 and 1 person cases
if len(sys.argv) < 2:
    print 'Please specify atleast two input times'
    sys.exit(0)
elif len(sys.argv) == 2:
    print 'Solution: ( 1 )',
    print ' Total Time: ', sys.argv[1], 'min'
    sys.exit(0)
    
# Read crossing time for each person from command-line
for x in xrange(1, len(sys.argv)):
    source.append(x)
    crossing_time[x] = int(sys.argv[x])

solve(source[:], dest[:], 0, 0, '', solution_set)

tmp = sorted(solution_set, key=lambda x: x[1])

for s in tmp:
    print 'Solution: (', s[0], ')',
    print ' Total Time: ', s[1], 'min'
    print '---------------------------------------------------'
