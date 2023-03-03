## 1. Call a different function from the statistics module

import statistics

nums = [8, 18, 42, 88, 8, 33, 26, 21, 99]

print(statistics.mean(nums))
print(statistics.stdev(nums))
print(statistics.fmean(nums))
print(statistics.harmonic_mean(nums))


## 2. Create a module named 'cubed' with a function that takes a number as a 
## parameter and returns the number cubed. Import and call the function from
## another module.

import cubed

result = cubed.cube_it(8)
print(result)
