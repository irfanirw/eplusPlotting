import pandas as pd
import datetime as dt
import os
import matplotlib.pyplot as plt


def get_folder_name(keyword):
    data_container = []
    for foldername in os.listdir():
        if keyword in foldername:
            data_container.append(foldername)
        else:
            pass
    return data_container

def read_all_csv(folder_list, selected_column):
    data_container = []
    total_files = len(folder_list)
    counter = 1
    for i in folder_list:
        df = pd.read_csv(i + '/OpenStudio/' + i + '/ModelToIdf/in.csv', usecols=selected_column)
        df['Date/Time'] = create_time()
        df1 = df.set_index(['Date/Time'])
        df1.index = pd.to_datetime(df1.index)
        df1.columns = [i]
        data_container.append(df1)

        print(f'{counter}/{total_files} DataFrame created, {total_files - counter} more files')
        counter +=1
    print('Generating DataFrame done\nConcatenating...')
    dataframe = pd.concat(data_container, axis=1)
    print("DataFrame ready")
    return dataframe

def create_time():
    date_time_column = []
    base_time = dt.datetime(2019, 1, 1)
    timedelta = dt.timedelta(hours=1)
    for i in range(8760):
        date_time_column.append(str(base_time))
        base_time +=timedelta
    return date_time_column

#def plot_option(df):
#    resample = ''
#    while (resample is not 'daily') or (resample is not 'monthly') or (resample is not 'hourly'):
#        resample = input("Choose your resample mapping (hourly, daily, or monthly): ")
#        if resample == 'hourly':
#            axes = df.resample("H").mean().plot(figsize=(18,6))
#            return axes
#        elif resample == 'daily':
#            axes = df.resample("D").mean().plot(figsize=(18,6))
#            return axes
#        elif resample == 'monthly':
#            axes = df.resample("M").mean().plot(figsize=(18,6))
#            return axes

if __name__ == '__main__':
    temperature_column = ['Date/Time', 'ROOM1:Zone Mean Air Temperature [C](Hourly)']
    file = get_folder_name('00')
    df = read_all_csv(file, temperature_column)
    ax = df.resample("D").mean().plot(figsize=(18,6))
    ax.legend(loc=2)
    ax.set_title(label='Far East Flora Dome Indoor Air Temperature Comparison', loc='center')
    ax.set_xlabel(xlabel='Date/Time')
    ax.set_ylabel(ylabel='Celsius Degree')

    plt.show()