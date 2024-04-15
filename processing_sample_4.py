import math
import json
import statistics


def extract_x_coordinates(all_data):
    """This function is used to extract x coordinates from the encoder data to find the distance moved in cm
    return single x coordinate value in float"""
    # To extract x axis coordinates
    raw_location = all_data['raw_location']
    encoder_left_front = raw_location['leftfront']
    # encoder_right_front = raw_location['rightfront']
    # encoder_left_rear = raw_location['leftrear']
    encoder_right_rear = raw_location['rightrear']

    print(encoder_left_front)
    # print(encoder_right_front)
    # print(encoder_left_rear)
    print(encoder_right_rear)
    print()

    encoder_average = (encoder_left_front + encoder_right_rear) / 2
    print("Encoder Average: " + str(encoder_average))
    print()

    x_coordinate = encoder_average / 350 * math.pi * 4.4  # this value is in cm
    return x_coordinate


def extract_z_coordinates(all_data):
    """This function is used to extract the REAL and IMAGE coordinates from the input 'all_data' with appropriate
    sensor readings, return two separate arrays holding each REAL and IMAGE coordinate and its length"""
    # for z axis coordinates
    length = 0
    z_coordinates_real = []
    z_coordinates_imag = []
    for channel_num in range(len(all_data['data'])):
        # print(channel_num)
        z_readings_single_channel_real = []
        z_readings_single_channel_imag = []

        for readings in all_data['data'][channel_num]:
            # Split real and img readings of a single channel into a list holding real and imaginary.
            z_readings_single_channel_real.append(readings[0])
            z_readings_single_channel_imag.append(readings[1])
        # print(z_readings_single_channel_real)
        # print(z_readings_single_channel_imag)
        # print()

        # process and find average
        z_average_single_channel_real = statistics.mean(z_readings_single_channel_real)
        z_average_single_channel_imag = statistics.mean(z_readings_single_channel_imag)

        # append them to lists of z axis
        z_coordinates_real.append(z_average_single_channel_real)
        z_coordinates_imag.append(z_average_single_channel_imag)
        # print(z_coordinates_real)
        # print(z_coordinates_imag)

        # finding length of the z axis
        length = len(z_coordinates_real)
        # print(length)

    return z_coordinates_real, z_coordinates_imag, length


def generate_x_y_marching_coordinates(x_coordinate, channel_separation, length):
    """This function returns the matching coordinates with the length specified by z coordinates data,
    return lists of x_coordinates, y_coordinates"""
    # generate x and y matching data arrays
    x_coordinates = []
    y_coordinates = []
    for i in range(length):
        x_coordinates.append(x_coordinate)
        y_coordinates.append(i * channel_separation)
    return x_coordinates, y_coordinates


def main(filename, channel_separation):
    """Main function of this data processing scripts"""
    print("Starting data processing scripts...")
    print("Loading data...")

    with open(filename) as f_obj:
        sample_data = json.load(f_obj)

    x_coordinates = []
    y_coordinates = []
    z_coordinates_real = []
    z_coordinates_imag = []

    for outer_layer_data in sample_data.values():
        for sample_num, all_data in outer_layer_data.items():
            print("Sample Number: " + str(sample_num))
            print()

            # extract z coordinates and number of data channels
            (z_coordinates_single_channel_real, z_coordinates_single_channel_imag,
             channel_length) = extract_z_coordinates(all_data)
            print("Current Sample Z coordinates: ")
            print(z_coordinates_single_channel_real)
            print(z_coordinates_single_channel_imag)
            print()

            z_coordinates_real.append(z_coordinates_single_channel_real)
            z_coordinates_imag.append(z_coordinates_single_channel_imag)

            # finding x coordinates for this group of reading.
            x_coordinate = extract_x_coordinates(all_data)

            # put x coordinates and y coordinates in a matching array with z coordinates
            x_sample_coordinates, y_sample_coordinates \
                = generate_x_y_marching_coordinates(x_coordinate, channel_separation, channel_length)
            print("X sample coordinates: ")
            print(x_sample_coordinates)
            print()
            print("Y sample coordinates: ")
            print(y_sample_coordinates)
            print()

            x_coordinates.append(x_sample_coordinates)
            y_coordinates.append(y_sample_coordinates)
        print("X coordinates:")
        print(x_coordinates)
        print()

        print("Y coordinates:")
        print(y_coordinates)
        print()

        print("Z coordinates:")
        print(z_coordinates_real)
        print(z_coordinates_imag)
        print()
    return x_coordinates, y_coordinates, z_coordinates_real, z_coordinates_imag


if "__main__" == __name__:
    filename = "Sample_data_2.json"
    channel_separation = 1  # enter channel separation distance in cm
    main(filename, channel_separation)
