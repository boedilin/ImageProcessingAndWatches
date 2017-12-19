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
beginning_led_on = 100
lower_limit_start_maximum = 300

directory = "path"
sadValues = np.loadtxt(directory+"path")
timestamps = np.loadtxt(directory+"path")

def is_maxima_search_window_5(array, index):
    left_right_increase = 2
    middle = 2
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
            index_in_search_window = middle
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
maximum = start_index
start_timestamp = timestamps[start_index]
while (maximum + step_size + search_window_increase) <= len(sadValues):
    next_maximum = is_maxima_search_window_5(sadValues, maximum + step_size)
    maxima.append(next_maximum)
    maximum = next_maximum
    durations_of_half_periods_in_microsec.append((timestamps[maximum] - start_timestamp) / len(maxima))

end_timestamp = timestamps[maximum]
duration_of_half_period_in_microsec = (end_timestamp - start_timestamp) / len(maxima)

print("start timestamp", start_timestamp)
print("end timestamp", end_timestamp)
print("number of found minimas", len(maxima))
print("average length of half period: ", duration_of_half_period_in_microsec)
print("rate deviation per day: ", (seconds_per_hour-((duration_of_half_period_in_microsec/microseconds_in_second)*strokes_per_hour))*hours_per_day)