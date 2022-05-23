"""
This script is used to add the bitrate and frame rate data to an external json file (list) as a new dictionary in the list.
"""
import json


def generate_new_data_set(sensor_mode,
                          resolution,
                          codec,
                          chroma_subsampling,
                          bit_depth,
                          frame_rate,
                          bitrate,
                          file_format):
    """
    generating a new set of data, return a dictionary
    for appending to the the camera list (for example fx6).
    """
    new_data_set = {}
    new_data_set.setdefault('sensor mode', sensor_mode)
    new_data_set.setdefault('resolution', resolution)
    new_data_set.setdefault('codec', codec)
    new_data_set.setdefault('chroma subsampling', chroma_subsampling)
    new_data_set.setdefault('bit depth', bit_depth)
    new_data_set.setdefault('frame rate', frame_rate)
    new_data_set.setdefault('bitrate', bitrate)
    new_data_set.setdefault('file format', file_format)
    return new_data_set


def get_from_json(file_path):
    """
    Get json file from given file_path and return that file.
    If given file_path doesn't exist, return None.
    """
    try:
        with open(file_path, 'r') as f:
            file = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return file


def write_to_json(file_path, new_dict):
    """
    Using get_from_json() to get file (list), then
    append given new_dict to that file (list).
    Finally, overwriting that file with new list.
    """
    fx6 = get_from_json(file_path)
    fx6.append(new_dict)
    with open(file_path, 'w') as f:
        json.dump(fx6, f)


filename = 'fx6_database.json'

n_d = generate_new_data_set('ff', 'uhd', 'xavci', 422, 10, 25, 250, 'mxf')
write_to_json(filename, n_d)