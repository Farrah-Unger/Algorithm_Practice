'''You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.


Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.'''

# Can I create a hash where they key is the total and the value is the pair of songs?
# initialize and empty hash pair_map
# initialize a counter to 0
# itierate through time array and % 60 the pairs
# find the difference with equation (remainder = (60 - time[i] % 60) % 60)
# check if the difference exists in the pair_maop as a key
# if it exists counter += 1 

def numPairsDivisbleBy60(time):
    counter = 0
    pair_map = {}
    for i in time:
        remainder = i % 60
        difference = (60 - remainder) % 60
        if difference in pair_map:
            counter += pair_map[difference]

        pair_map[remainder] = pair_map.get(remainder, 0) + 1
    return counter

    # count = 0
    # n = len(time)

    # for i in range(n - 1):
    #     for j in range(i + 1, n):
    #         if (time[i] + time[j]) % 60 == 0:
    #             count += 1

    # return count



print(numPairsDivisbleBy60([30,20,150,100,40]))
# print(numPairsDivisbleBy60([60,60,60]))
