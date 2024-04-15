import matplotlib.pyplot as plt
import processing_sample_4

# Update filename to have different results
# Update channel separation to change the scale in y-axis
# All graphs are drawn to the cm (centimeter) scale
filename = "test_0322.json"
channel_separation = 1
offset_group_num = 56

def plot_3d_data(x, y, z, size=50):
    plt.scatter(x, y, c=z, cmap='viridis', marker='s', s=size)  # 's' specifies square marker, size parameter adjusts the size
    plt.colorbar(label='z')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('2D Diagram with Z represented by Color')
    plt.grid(True)
    plt.show()



def main():
    # Define x, y, and z coordinates
    # x_values = [[0,1,2], [3,4,5]]
    # y_values = [[0,2,2], [3,4,5]]  # Values from 1 to 10
    # z_values = np.arange(1, 7)  # Values from 1 to 10

    # Get arrays for x, y, z_real and z_imag coordinates
    (x_values, y_values,
     z_coordinates_real, z_coordinates_imag) = processing_sample_4.main(filename, channel_separation)

    # Plotting the data with adjusted size
    plot_3d_data(x_values, y_values, z_coordinates_real, size=30)  # Adjust size as needed
    plot_3d_data(x_values, y_values, z_coordinates_imag, size=30)  # Adjust size as needed

if __name__ == "__main__":
    main()
