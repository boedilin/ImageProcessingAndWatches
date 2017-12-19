import numpy as np
import math

watch_hertz = 2.5
frames_per_second = 90
hours_per_day = 24
seconds_per_hour = 3600
one_second = 1
microseconds_in_second = 1000000
strokes_per_hour = 2 * watch_hertz * seconds_per_hour
watch_hertz_half_period = watch_hertz * 2
half_period_duration_in_sec = one_second / watch_hertz_half_period
resolution_grid_in_sec = one_second / frames_per_second
step_size = math.ceil(half_period_duration_in_sec / resolution_grid_in_sec)

directory = "greiner/14.12.17/run5_+20sec_greiner/"
xValues = np.loadtxt(directory+"yValues.txt")
timestamps = np.loadtxt(directory+"timestamps.txt")

def is_minima_search_window_5(array, index):
    left_right_increase = 2
    if index+left_right_increase < len(array):
        search_window = np.copy(array[index-left_right_increase-1:index+left_right_increase])
        array_to_find_index = np.copy(array[index-left_right_increase-1:index+left_right_increase])
        search_window.sort()
        minima = search_window[0]
        index_in_search_window = np.where(array_to_find_index == minima)[0][0]
        return index + (index_in_search_window - left_right_increase)

def find_start_minima(array):
    first_20_x_values = np.copy(array[:20])
    first_20_x_values.sort()
    if first_20_x_values[0] == 0:
        return np.where(array[:20] == first_20_x_values[1])[0][0]
    else :
        return np.where(array[:20] == first_20_x_values[0])[0][0]

durations_of_half_periods_in_microsec = []
search_window_increase = 2
minimas = []
start_index = find_start_minima(xValues)
minima = start_index
start_timestamp = timestamps[start_index]
while (minima + step_size + search_window_increase) <= len(xValues):
    next_minima = is_minima_search_window_5(xValues, minima + step_size)
    minimas.append(next_minima)
    minima = next_minima
    durations_of_half_periods_in_microsec.append((timestamps[minima] - start_timestamp) / len(minimas))

end_timestamp = timestamps[minima]
duration_of_half_period_in_microsec = (end_timestamp - start_timestamp) / len(minimas)

print(start_timestamp)
print(end_timestamp)
print

print("start timestamp", start_timestamp)
print("end timestamp", end_timestamp)
print("number of found minimas", len(minimas))
print("length of half period over all: ", duration_of_half_period_in_microsec)
print("variation per day: ", (3600-((duration_of_half_period_in_microsec/microseconds_in_second)*strokes_per_hour))*hours_per_day)