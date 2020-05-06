from EnergyPlot import get_energy_number, construct_dict
import TemperaturePlot
from TemperaturePlot import get_folder_name
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # generate energy dataframe
    folder_names = get_folder_name('00')
    energy_number = get_energy_number(folder_names)
    df_energy = construct_dict(folder_names, energy_number)

    # generate temperature dataframe
    temperature_column = ['Date/Time', 'ROOM1:Zone Mean Air Temperature [C](Hourly)']
    file = get_folder_name('00')
    df = TemperaturePlot.read_all_csv(file, temperature_column)
    df1 = df.transpose()
    df2 = df1.mean(axis=1)
    df_temp = pd.DataFrame(df2)
    df_temp.columns = ["Temperature"]

    # combine both data
    combined = pd.concat([df_energy, df_temp], axis=1)

    # scatter plot
    ax = combined.plot.scatter(x='Energy Use Intensity', y='Temperature')
    ax.set_title(label='Energy Use Intensity and Temperature', loc='center')
    plt.show()