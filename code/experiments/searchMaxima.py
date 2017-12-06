#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:16:42 2017

@author: Linda
"""

# pylint: disable=invalid-name
import numpy as np
import math

frames_per_second = 90
one_second = 1
watch_hertz = 3
watch_hertz_half_period = watch_hertz * 2
half_period_duration_in_sec = one_second / watch_hertz_half_period
resolution_grid_in_sec = one_second / frames_per_second
step_size = math.ceil(half_period_duration_in_sec / resolution_grid_in_sec)
beginning_led_on = 100
lower_limit_start_maximum = 300

directory = "records_from_led_board/sadValues/2400sec/"
sadValues = np.loadtxt(directory+"cutoff_sad_values_2400_sec_run_5.txt")
timestamps = np.loadtxt(directory+"cutoff_timestamps_2400_sec_run_5.txt")

def is_maxima_search_window_5(array, index):
    left_right_increase = 2
    if index+left_right_increase < len(array):
        search_window = np.copy(array[index-left_right_increase-1:index+left_right_increase])
        array_to_find_index = np.copy(array[index-left_right_increase-1:index+left_right_increase])
        maxima = "unset"
        for i in search_window:
            if i > beginning_led_on:
                maxima = i
                break
        if maxima == "unset":
            print("never found a maxima at: ", index)
        try:
            index_in_search_window = np.where(array_to_find_index == maxima)[0][0]
        except:
            index_in_search_window = 2
        return index + (index_in_search_window - left_right_increase)

def find_start_maxima(array):
    first_30_x_values = np.copy(array[:30])
    for i in first_30_x_values:
            if i > lower_limit_start_maximum:
                return np.where(array[:30] == i)[0][0]

durations_of_half_periods_in_microsec = []
search_window_increase = 2
maxima = []

start_index = find_start_maxima(sadValues)
#print("start index: ", start_index)
#start_index = 18
maximum = start_index
start_timestamp = timestamps[start_index]
while (maximum + step_size + search_window_increase) < len(sadValues):
    next_maximum = is_maxima_search_window_5(sadValues, maximum + step_size)
    maxima.append(next_maximum)
    maximum = next_maximum
    durations_of_half_periods_in_microsec.append((timestamps[maximum] - start_timestamp) / len(maxima))

end_timestamp = timestamps[maximum]
duration_of_half_period_in_microsec = (end_timestamp - start_timestamp) / len(maxima)

for value in range(len(durations_of_half_periods_in_microsec)):
    durations_of_half_periods_in_microsec[value] = abs(durations_of_half_periods_in_microsec[value]-166666)

durations_of_half_periods_in_microsec.sort()

print("smallest aberration found during calculation: ", durations_of_half_periods_in_microsec[0])
print("start timestamp", start_timestamp)
print("end timestamp", end_timestamp)
print("number of found minimas", len(maxima))
print("length of half period over all: ", duration_of_half_period_in_microsec)
print("variation per day: ", ((duration_of_half_period_in_microsec/1000000*21600)-3600)*24)