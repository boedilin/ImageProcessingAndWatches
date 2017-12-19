import numpy as np
import math

watch_hertz = 3
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

directory = "path"
xValues = np.loadtxt(directory+"path")
timestamps = np.loadtxt(directory+"path")

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

durations_of_period_in_microsec = []
durations_of_period_in_microsec_tic = []
durations_of_period_in_microsec_toc = []
search_window_increase = 2
minima_tic = []
minima_toc = []
start_index = find_start_minima(xValues)
minima = start_index
switch_to_tic = False
counter_tic = 0
counter_toc = 0
start_timestamp = timestamps[start_index]
while (minima + step_size + search_window_increase) <= len(xValues):
    next_minima = is_minima_search_window_5(xValues, minima + step_size)
    if switch_to_tic:
        minima_tic.append(next_minima)
        switch_to_tic = False
        counter_tic = counter_tic + 1
        if counter_tic % 2 == 0:
            durations_of_period_in_microsec_tic.append((timestamps[minima_tic[-1]] - timestamps[minima_tic[-2]]))
    else:
        minima_toc.append(next_minima)
        switch_to_tic = True
        counter_toc = counter_toc + 1
        if counter_toc % 2 == 0:
            durations_of_period_in_microsec_toc.append((timestamps[minima_toc[-1]] - timestamps[minima_toc[-2]]))
    minima = next_minima
    if len(durations_of_period_in_microsec_tic) > 0 and len(durations_of_period_in_microsec_toc) > 0:
        durations_of_period_in_microsec.append((durations_of_period_in_microsec_tic[-1]+durations_of_period_in_microsec_toc[-1])/2)

end_timestamp = timestamps[minima]
duration_of_period_in_microsec = np.sum(durations_of_period_in_microsec) / len(durations_of_period_in_microsec)

print("start timestamp", start_timestamp)
print("end timestamp", end_timestamp)
print("number of found minimas", len(minima_tic)+len(minima_toc))
print("average length of half period: ", duration_of_period_in_microsec/2)
print("rate deviation per day: ", (seconds_per_hour-(((duration_of_period_in_microsec/2)/microseconds_in_second)*strokes_per_hour))*hours_per_day)