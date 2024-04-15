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

    # print(encoder_left_front)
    # print(encoder_right_front)
    # print(encoder_left_rear)
    # print(encoder_right_rear)
    # print()

    encoder_average = (encoder_left_front + encoder_right_rear) / 2
    # print("Encoder Average: " + str(encoder_average))
    # print()

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

    return z_coordinates_real, z_coordinates_imag


def offset_subtraction(offset, original_data):
    """Offset and original_data are both 1D arrays with the same number of elements.
    Subtract elements with the same index from offset and original_data and return data array as data"""
    length = len(offset)
    data = []

    for index in range(length):
        processed_num = original_data[index] - offset[index]
        data.append(processed_num)

    return data


def main(filename):
    """Main function of this data processing scripts"""
    print("Starting data processing scripts...")
    print("Loading data...")

    with open(filename) as f_obj:
        sample_data = json.load(f_obj)

    x_coordinates = []
    z_coordinates_real = []
    z_coordinates_imag = []

    z_real_offset, z_imag_offset = extract_z_coordinates(sample_data['0']['0'])
    # print("z real offset: ")
    # print(z_real_offset)

    # print("z imag offset")
    # print(z_imag_offset)

    for outer_layer_data in sample_data.values():
        for sample_num, all_data in outer_layer_data.items():
            # print("Sample Number: " + str(sample_num))
            # print()

            # extract z coordinates and number of data channels
            (z_coordinates_single_channel_real, z_coordinates_single_channel_imag,
             ) = extract_z_coordinates(all_data)
            # print("Current Sample Z coordinates: ")
            # print(z_coordinates_single_channel_real)
            # print(z_coordinates_single_channel_imag)
            # print()

            z_real_processed = offset_subtraction(z_real_offset, z_coordinates_single_channel_real)
            # print("Z processed after offset")
            # print(z_real_processed)

            z_imag_processed = offset_subtraction(z_imag_offset, z_coordinates_single_channel_imag)

            z_coordinates_real.append(z_real_processed)
            z_coordinates_imag.append(z_imag_processed)

            # finding x coordinates for this group of reading.
            x_coordinate = extract_x_coordinates(all_data)
            x_coordinates.append(x_coordinate)

        # print("X coordinates:")
        # print(x_coordinates)
        # print()


        # print("Z coordinates:")
        # print(z_coordinates_real)
        # print(z_coordinates_imag)
        # print()
    return x_coordinates, z_coordinates_real, z_coordinates_imag


if "__main__" == __name__:
    filename = "Sample_data_2.json"
    main(filename)
