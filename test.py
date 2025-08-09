from sort import sort, STANDARD, SPECIAL, REJECTED

# Standard Test

## Standard
w, h, l, m = 10, 10, 10, 10
assert sort(w, h, l, m) == STANDARD

# Special Test

## Weight GTE 20
w, h, l, m = 10, 10, 10, 20
assert sort(w, h, l, m) == SPECIAL

## One dimension GTE 150    
w, h, l, m = 150, 10, 10, 10
assert sort(w, h, l, m) == SPECIAL

## Volume GTE 1_000_000
w, h, l, m = 100, 100, 100, 10
assert sort(w, h, l, m) == SPECIAL

# Rejected Test

## Volume GTE 1_000_000 and weight GTE 20
w, h, l, m = 100, 100, 100, 20
assert sort(w, h, l, m) == REJECTED
