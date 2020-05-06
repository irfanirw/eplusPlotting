import pandas as pd
from TemperaturePlot import get_folder_name
import matplotlib.pyplot as plt

def get_energy_number(folder_names):
    count = 1
    data_container = []
    for i in folder_names:
        text_data = open(i + '/OpenStudio/' + i + '/ModelToIdf/inTable.csv').read().splitlines()
        for j in text_data:
            count += 1
            if 'Total Site Energy' in j:
                number = j.split(',')[3]
                number_float = float(number)
                data_container.append(number_float*0.277778)
            else:
                pass
    return data_container

def construct_dict(filename, energy_number):
    keys = filename
    values = energy_number
    df = pd.DataFrame(values, keys)
    df.columns = ['Energy Use Intensity']
    return df

if __name__ == '__main__':
    folder_names = get_folder_name('00')
    energy_number = get_energy_number(folder_names)
    df = construct_dict(folder_names, energy_number)
    ax = df.plot.bar(grid=True)
    ax.set_ylabel(ylabel='kWh/M2')
    ax.set_xlabel(xlabel='Dome Type')
    plt.show()