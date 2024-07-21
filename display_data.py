import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

def display_data(data: List[Tuple[str, int]]):
    """Displays the dishes and their quantities in a table using matplotlib.
    """
    # Extract columns for the table
    dishes = [item[0] for item in data]
    quantities = [item[1] for item in data]

    # Define table data
    table_data = list(zip(dishes, quantities))

    # Create a new figure
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the size as needed

    # Hide the axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    # Create the table
    table = plt.table(cellText=table_data, colLabels=['Món ăn', 'Số lượng'], cellLoc='center', loc='center')

    # Adjust table appearance
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.auto_set_column_width([0, 1])  # Adjust column width

    # Save the figure as an image
    plt.savefig('dishes_table.png', bbox_inches='tight', pad_inches=0.1)
    plt.show()
