#! /usr/bin/env python3


from operator import add
import sys

string = []
with open("input.txt", "r") as f:
    string = ''.join(f.readlines())


INPUT = string.strip().split(',')
MOVES = {
    'n':  ( 0,  1, -1),
    'ne': ( 1,  0, -1),
    'se': ( 1, -1,  0),
    's':  ( 0, -1,  1),
    'sw': (-1,  0,  1),
    'nw': (-1,  1,  0)
}

p = (0, 0, 0)
dist = furthest = 0

for step in INPUT:
    p = tuple(map(add, p, MOVES[step]))
    dist = max(map(abs, p))
    furthest = max(dist, furthest)

print([dist, furthest])
