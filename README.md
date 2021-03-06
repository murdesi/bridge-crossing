# bridge-crossing
Python program to solve bridge-crossing puzzle

N persons want to cross a bridge at night. Two persons can cross at a time sharing one torch. One person has to return with the torch. The N persons cross the bridge at different speeds. When a pair cross the bridge, their speed is determined by the slowest of them. The objective of the puzzle is to find the combination of persons going back and forth until all persons are on the other side in the
least possible amount of time.

Requirements

Python 2.7 or above

Usage:

python puzzle.py time_for_person1 time_for_person2 ... time_for_personN

Example:

python puzzle.py 1 2 7 10

where, time taken for person 1 to cross the bridge is 1 min, for person 2 it is 2 mins and so on

Output:

In the Solution string below, M+N indicates that person M and person N cross to the other side. A single number N indicates that person N crosses back to the starting point.

Solution: ( 1+2, 1, 3+4, 2, 1+2 )  Total Time:  17 min
---------------------------------------------------
Solution: ( 1+2, 2, 3+4, 1, 2+1 )  Total Time:  17 min
---------------------------------------------------
Solution: ( 1+2, 1, 3+1, 1, 4+1 )  Total Time:  21 min
---------------------------------------------------
Solution: ( 1+2, 1, 4+1, 1, 3+1 )  Total Time:  21 min
---------------------------------------------------
Solution: ( 1+3, 1, 2+1, 1, 4+1 )  Total Time:  21 min
---------------------------------------------------
Solution: ( 1+3, 1, 4+1, 1, 2+1 )  Total Time:  21 min
---------------------------------------------------
Solution: ( 1+4, 1, 2+1, 1, 3+1 )  Total Time:  21 min
---------------------------------------------------
Solution: ( 1+4, 1, 3+1, 1, 2+1 )  Total Time:  21 min
---------------------------------------------------
Solution: ( 1+2, 1, 3+1, 2, 4+2 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+2, 1, 4+1, 2, 3+2 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+2, 2, 3+2, 1, 4+1 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+2, 2, 4+2, 1, 3+1 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+3, 1, 2+4, 2, 1+2 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+3, 1, 2+1, 2, 4+2 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+4, 1, 2+3, 2, 1+2 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+4, 1, 2+1, 2, 3+2 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 2+3, 2, 1+4, 1, 2+1 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 2+3, 2, 1+2, 1, 4+1 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 2+4, 2, 1+3, 1, 2+1 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 2+4, 2, 1+2, 1, 3+1 )  Total Time:  22 min
---------------------------------------------------
Solution: ( 1+2, 2, 3+2, 2, 4+2 )  Total Time:  23 min
---------------------------------------------------
Solution: ( 1+2, 2, 4+2, 2, 3+2 )  Total Time:  23 min
---------------------------------------------------
Solution: ( 2+3, 2, 1+2, 2, 4+2 )  Total Time:  23 min
---------------------------------------------------
Solution: ( 2+3, 2, 4+2, 2, 1+2 )  Total Time:  23 min
---------------------------------------------------
Solution: ( 2+4, 2, 1+2, 2, 3+2 )  Total Time:  23 min
---------------------------------------------------
Solution: ( 2+4, 2, 3+2, 2, 1+2 )  Total Time:  23 min
---------------------------------------------------
Solution: ( 1+2, 1, 3+4, 3, 1+3 )  Total Time:  27 min
---------------------------------------------------
Solution: ( 1+2, 1, 3+1, 3, 4+3 )  Total Time:  27 min
---------------------------------------------------
Solution: ( 1+3, 1, 2+1, 3, 4+3 )  Total Time:  27 min
---------------------------------------------------
Solution: ( 1+3, 3, 4+3, 1, 2+1 )  Total Time:  27 min
---------------------------------------------------
Solution: ( 3+4, 3, 1+2, 1, 3+1 )  Total Time:  27 min
---------------------------------------------------
Solution: ( 3+4, 3, 1+3, 1, 2+1 )  Total Time:  27 min
---------------------------------------------------
Solution: ( 1+2, 2, 3+4, 3, 2+3 )  Total Time:  28 min
---------------------------------------------------
Solution: ( 1+2, 2, 3+2, 3, 4+3 )  Total Time:  28 min
---------------------------------------------------
Solution: ( 2+3, 2, 1+2, 3, 4+3 )  Total Time:  28 min
---------------------------------------------------
Solution: ( 2+3, 3, 4+3, 2, 1+2 )  Total Time:  28 min
---------------------------------------------------
Solution: ( 3+4, 3, 1+2, 2, 3+2 )  Total Time:  28 min
---------------------------------------------------
Solution: ( 3+4, 3, 2+3, 2, 1+2 )  Total Time:  28 min
---------------------------------------------------
Solution: ( 1+3, 1, 2+4, 3, 1+3 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 1+3, 1, 4+1, 3, 2+3 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 1+3, 3, 2+4, 1, 3+1 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 1+3, 3, 2+3, 1, 4+1 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 1+4, 1, 2+3, 3, 1+3 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 1+4, 1, 3+1, 3, 2+3 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 2+3, 3, 1+4, 1, 3+1 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 2+3, 3, 1+3, 1, 4+1 )  Total Time:  32 min
---------------------------------------------------
Solution: ( 1+2, 1, 3+4, 4, 1+4 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 1+2, 1, 4+1, 4, 3+4 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 1+3, 3, 2+4, 2, 3+2 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 1+3, 3, 2+3, 2, 4+2 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 1+4, 1, 2+1, 4, 3+4 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 1+4, 4, 3+4, 1, 2+1 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 2+3, 2, 1+4, 3, 2+3 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 2+3, 2, 4+2, 3, 1+3 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 2+3, 3, 1+4, 2, 3+2 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 2+3, 3, 1+3, 2, 4+2 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 2+4, 2, 1+3, 3, 2+3 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 2+4, 2, 3+2, 3, 1+3 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 3+4, 4, 1+2, 1, 4+1 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 3+4, 4, 1+4, 1, 2+1 )  Total Time:  33 min
---------------------------------------------------
Solution: ( 1+2, 2, 3+4, 4, 2+4 )  Total Time:  34 min
---------------------------------------------------
Solution: ( 1+2, 2, 4+2, 4, 3+4 )  Total Time:  34 min
---------------------------------------------------
Solution: ( 2+4, 2, 1+2, 4, 3+4 )  Total Time:  34 min
---------------------------------------------------
Solution: ( 2+4, 4, 3+4, 2, 1+2 )  Total Time:  34 min
---------------------------------------------------
Solution: ( 3+4, 4, 1+2, 2, 4+2 )  Total Time:  34 min
---------------------------------------------------
Solution: ( 3+4, 4, 2+4, 2, 1+2 )  Total Time:  34 min
---------------------------------------------------
Solution: ( 1+3, 1, 2+4, 4, 1+4 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+3, 1, 4+1, 4, 2+4 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+3, 3, 2+3, 3, 4+3 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+3, 3, 4+3, 3, 2+3 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+4, 1, 2+3, 4, 1+4 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+4, 1, 3+1, 4, 2+4 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+4, 4, 2+3, 1, 4+1 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+4, 4, 2+4, 1, 3+1 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 2+3, 3, 1+3, 3, 4+3 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 2+3, 3, 4+3, 3, 1+3 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 2+4, 4, 1+3, 1, 4+1 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 2+4, 4, 1+4, 1, 3+1 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 3+4, 3, 1+3, 3, 2+3 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 3+4, 3, 2+3, 3, 1+3 )  Total Time:  38 min
---------------------------------------------------
Solution: ( 1+4, 4, 2+3, 2, 4+2 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 1+4, 4, 2+4, 2, 3+2 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 2+3, 2, 1+4, 4, 2+4 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 2+3, 2, 4+2, 4, 1+4 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 2+4, 2, 1+3, 4, 2+4 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 2+4, 2, 3+2, 4, 1+4 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 2+4, 4, 1+3, 2, 4+2 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 2+4, 4, 1+4, 2, 3+2 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 3+4, 3, 1+2, 4, 3+4 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 3+4, 4, 1+2, 3, 4+3 )  Total Time:  39 min
---------------------------------------------------
Solution: ( 1+3, 3, 2+4, 4, 3+4 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 1+3, 3, 4+3, 4, 2+4 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 1+4, 4, 2+3, 3, 4+3 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 1+4, 4, 3+4, 3, 2+3 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 2+3, 3, 1+4, 4, 3+4 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 2+3, 3, 4+3, 4, 1+4 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 2+4, 4, 1+3, 3, 4+3 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 2+4, 4, 3+4, 3, 1+3 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 3+4, 3, 1+3, 4, 2+4 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 3+4, 3, 2+3, 4, 1+4 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 3+4, 4, 1+4, 3, 2+3 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 3+4, 4, 2+4, 3, 1+3 )  Total Time:  44 min
---------------------------------------------------
Solution: ( 1+4, 4, 2+4, 4, 3+4 )  Total Time:  50 min
---------------------------------------------------
Solution: ( 1+4, 4, 3+4, 4, 2+4 )  Total Time:  50 min
---------------------------------------------------
Solution: ( 2+4, 4, 1+4, 4, 3+4 )  Total Time:  50 min
---------------------------------------------------
Solution: ( 2+4, 4, 3+4, 4, 1+4 )  Total Time:  50 min
---------------------------------------------------
Solution: ( 3+4, 4, 1+4, 4, 2+4 )  Total Time:  50 min
---------------------------------------------------
Solution: ( 3+4, 4, 2+4, 4, 1+4 )  Total Time:  50 min
---------------------------------------------------
