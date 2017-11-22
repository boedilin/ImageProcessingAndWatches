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

"""
xysadValues = np.load("motion_vectors_10min_black_white.npy")
xValues = xysadValues[:, 0]
"""
directory = "different_position_records/down/8hours/"
xValues = np.loadtxt(directory+"xValues.txt")
timestamps = np.loadtxt(directory+"timestamps.txt")
indexes_of_minimas_file = open(directory+"indexes_of_minimas_file.txt", "a")
step_size_while_searching_file = open(directory+"step_sizes_file.txt", "a")

def is_minima_search_window_3(array, index, last_index):
    left_decrease = 2
    right_increase = 1
    if index+left_decrease < len(array):
        search_window = np.copy(array[index-left_decrease:index+right_increase])
        array_to_find_index = np.copy(array[index-left_decrease:index+right_increase])
        search_window.sort()
        minima = search_window[0]
        index_in_search_window = np.where(array_to_find_index == minima)[0][0]
        new_index = index + (index_in_search_window - right_increase)
        step_size_while_searching_file.write(str((new_index-last_index))+"\n")
        return new_index

def find_start_minima(array):
    """
    returns the index of the lowest value from first 20 values. this must be a stillstand.
    """
    first_20_x_values = np.copy(array[:20])
    first_20_x_values.sort()
    if first_20_x_values[0] == 0:
        return np.where(array[:20] == first_20_x_values[1])[0][0]
    else :
        return np.where(array[:20] == first_20_x_values[0])[0][0]

last_index = 1
indexes_of_minimas = [0] * len(xValues)
false_step_size_counter = 0
durations_of_half_periods_in_microsec = []
search_window_increase = 2
minimas = []
start_index = find_start_minima(xValues)
print("first minima at index: ", start_index)
minima = start_index
start_timestamp = timestamps[start_index]
while (minima + step_size + search_window_increase) <= len(xValues):
    next_minima = is_minima_search_window_3(xValues, minima + step_size, last_index)
    last_index = next_minima
    #print(next_minima-(minima+step_size))
    if next_minima != (minima + step_size):
        false_step_size_counter = false_step_size_counter + 1
    minimas.append(next_minima)
    indexes_of_minimas[next_minima-1] = 1
    minima = next_minima
    durations_of_half_periods_in_microsec.append((timestamps[minima] - start_timestamp) / len(minimas))

end_timestamp = timestamps[minima-1]
duration_of_half_period_in_microsec = (end_timestamp - start_timestamp) / (len(minimas)-1)

for value in range(len(durations_of_half_periods_in_microsec)):
    durations_of_half_periods_in_microsec[value] = abs(durations_of_half_periods_in_microsec[value]-166666)

durations_of_half_periods_in_microsec_file = open("durations_of_half_periods_in_microsec.txt", "a")

for index in range(len(indexes_of_minimas)):
    indexes_of_minimas_file.write(str(indexes_of_minimas[index])+"\n")

for index in range(len(durations_of_half_periods_in_microsec)):
    durations_of_half_periods_in_microsec_file.write(str(durations_of_half_periods_in_microsec[index])+"\n")
durations_of_half_periods_in_microsec.sort()
#print("median: ", durations_of_half_periods_in_microsec[math.floor(len(durations_of_half_periods_in_microsec)/2)])
print("smallest aberration found during calculation: ", durations_of_half_periods_in_microsec[0])
print("start timestamp", start_timestamp)
print("end timestamp", end_timestamp)
print("number of found minimas", len(minimas)-1)
print("length of half period over all: ", duration_of_half_period_in_microsec)
print("variation per day: ", ((duration_of_half_period_in_microsec/1000000*21600)-3600)*24)
print("step size wasnt correct: ", false_step_size_counter)