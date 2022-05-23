"""
This script is used to add the bitrate and frame rate data
to an external json file (list) as a new dictionary in the list.
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


def get_from_json(camera):
    """
    Get json file from given file_path and return that file.
    If given file_path doesn't exist, return None.
    """
    file_path = f"{camera}_database.json"
    while True:
        try:
            with open(file_path, 'r') as f:
                file = json.load(f)
        except FileNotFoundError:
            create_new_json(camera)
            continue
        else:
            return file


def create_new_json(camera):
    """
    Create new json file using given camera name as prefix.
    Don't return anything, simply create new file. If that
    file do exist, it will overwrite it with an empty list.
    """
    new_json_name = f"{camera}_database.json"
    with open(new_json_name, 'w') as f:
        json.dump([], f)


def write_to_json(camera, new_dict):
    """
    Using get_from_json() to get file (list), then
    append given new_dict to that file (list).
    Finally, overwriting that file with new list.
    """
    file_path = f"{camera}_database.json"
    cam = get_from_json(camera)
    cam.append(new_dict)
    with open(file_path, 'w') as f:
        json.dump(cam, f)


# filename = 'fx6_database.json'

n_d = generate_new_data_set('ff', 'uhd', 'xavcsi', 422, 10, 25, 250, 'mp4')
write_to_json('fx3', n_d)

# create_new_json('fx3')