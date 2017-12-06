import numpy as np

framerate = 90
first_second = framerate
directory = ""
records=[10,20,40,60,300,600,900,1200,1500,1800,2100,2400]
runs = [1,2,3,4,5]

for folder_index in records:
    folder_name = str(folder_index)+"sec"
    for run in runs:
        sad_file_path = folder_name+"/sad_values_"+str(folder_index)+"_sec_run_"+str(run)+".txt"
        timestamp_file_path = folder_name+"/timestamps_"+str(folder_index)+"_sec_run_"+str(run)+".txt"
        sad_values = np.loadtxt(sad_file_path)
        timestamp_values = np.loadtxt(timestamp_file_path)
        if len(sad_values) != len(timestamp_values):
            print("Eeeeeeeerorrrrrrrrr!!!! sad and timestamps has not same length", sad_file_path, ":::::", timestamp_file_path)
        
        for index in range(90,len(sad_values)):
            new_sad_file = open(folder_name+"/cutoff_sad_values_"+str(folder_index)+"_sec_run_"+str(run)+".txt", "a")
            new_timestamp_file = open(folder_name+"/cutoff_timestamps_"+str(folder_index)+"_sec_run_"+str(run)+".txt", "a")
            new_sad_file.write(str(sad_values[index])+"\n")
            new_timestamp_file.write(str(timestamp_values[index])+"\n")

        new_sad_file.close()
        new_timestamp_file.close()