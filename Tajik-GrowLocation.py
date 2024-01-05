import pandas as pd
import matplotlib.pyplot as plt

def read_and_rename_columns(data_file):
    '''
    Reads the CSV data and extracts latitude and longitude, swapping their names.
    
    Args:
        data_file (str): Path to the CSV data file.
        
    Returns:
        pandas.DataFrame: DataFrame with latitude and longitude columns renamed.
    '''
    # Read CSV file
    raw_data = pd.read_csv(data_file)
    
    # Extract latitude and longitude columns and rename them
    raw_data = raw_data[['Longitude', 'Latitude']]  # Swapped the column order
    raw_data.rename(columns={'Longitude': 'latitude', 'Latitude': 'longitude'}, inplace=True)
    
    return raw_data

def filter_outliers(dataframe):
    '''Filters outliers based on predefined upper and lower limits.'''
    # Apply lower limit filter
    lower_limit = dataframe.loc[(dataframe['latitude'] >= 50.681) & (dataframe['longitude'] >= -10.592)]
    
    # Apply upper limit filter
    final_data = lower_limit.loc[(lower_limit['latitude'] <= 57.985) & (lower_limit['longitude'] <= 1.6848)]
    return final_data


def plot_geo_locations(x_values, y_values, map_image_path='map7.png', save_path='Tajik_Visualized_Geo_Locations.png', title='Visualization of Geo Locations', x_label='Longitude', y_label='Latitude', figure_size=(10, 8), dpi=100):
    '''
    Plots geo-location data on the map.

    Parameters:
    - x_values (list): List of longitude values.
    - y_values (list): List of latitude values.
    - map_image_path (str): Path to the map image (default is 'map7.png').
    - save_path (str): Path to save the final plot (default is 'Visualized_Geo_Locations.png').
    - title (str): Title of the plot (default is 'Visualization of Geo Locations').
    - x_label (str): Label for the x-axis (default is 'Longitude').
    - y_label (str): Label for the y-axis (default is 'Latitude').
    - figure_size (tuple): Figure size in inches (default is (10, 8)).
    - dpi (int): Dots per inch for the saved image (default is 100).
    '''
    # Create figure and axis for the plot
    fig, ax = plt.subplots(figsize=figure_size)

    # Set plot title and axis labels
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    try:
        # Read the map image and set it as the background
        map_image = plt.imread(map_image_path)
        ax.imshow(map_image, extent=(-10.5, 1.8, 50.6, 57.8))
    except FileNotFoundError:
        print(f"Error: Map image not found at {map_image_path}. Make sure the path is correct.")

    # Plot longitudes and latitudes on the map
    ax.scatter(x_values, y_values) 

    # Save the final plot in the specified path
    fig.savefig(save_path)
    print(f"Plot saved at {save_path}")

def VisualizeGeoLocations(data_file):
    '''Orchestrates the process of visualizing geo-location data.'''
    # Read and rename columns
    dataframe = read_and_rename_columns(data_file)
    
    # Filter outliers from the dataset
    dataframe = filter_outliers(dataframe)

    # Extract values for plotting
    y_values = dataframe['latitude']
    x_values = dataframe['longitude']
    
    # Plot geo-locations on the map
    plot_geo_locations(x_values, y_values)
if __name__ == '__main__':
    file_path = 'GrowLocations.csv'
    VisualizeGeoLocations(data_file=file_path)
