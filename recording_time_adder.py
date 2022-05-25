"""
This script is used to add bitrate, frame rate and other parameters
to an external json file as a simple database, which is a list inside
it, with multiple dictionaries containing parameters.

If that json file already exist, simply add given parameter dictionary
to it. If that file does not exist, this script can create it automatically
based on the information you provided such like filename.
"""
import json


def generate_new_data_set(
    sensor_mode,
    resolution,
    codec,
    chroma_subsampling,
    bit_depth,
    frame_rate,
    file_format,
    bitrate
):
    """
    Generate a new set of parameters, return a dictionary
    for appending to the external json file list.
    """
    new_data_set = {}
    new_data_set.setdefault('sensor mode', sensor_mode)
    new_data_set.setdefault('resolution', resolution)
    new_data_set.setdefault('codec', codec)
    new_data_set.setdefault('chroma subsampling', chroma_subsampling)
    new_data_set.setdefault('bit depth', bit_depth)
    new_data_set.setdefault('frame rate', frame_rate)
    new_data_set.setdefault('file format', file_format)
    new_data_set.setdefault('bitrate', bitrate)
    return new_data_set


def get_from_json(camera):
    """
    Get json file from given camera name (function can
    automatically convert camera name to the corresponding
    file name) and returns the content of that file.

    If given name of the file doesn't exist, it will call
    create_new_json() function to create it.
    """
    file_path = f"data/{camera}_database.json"
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
    file does exist, it will overwrite it with an empty list.
    """
    new_json_name = f"data/{camera}_database.json"
    with open(new_json_name, 'w') as f:
        json.dump([], f)


def write_to_json(camera, new_dict):
    """
    Using get_from_json() to get json (if it's not exist,
    get_from_json() will call create_new_json() to create
    one), assign it to variable cam_para.

    Next, append given new_dict to cam_para.

    Finally, overwriting that file with new list (cam_para).
    """
    file_path = f"data/{camera}_database.json"
    cam_para = get_from_json(camera)
    cam_para.append(new_dict)
    with open(file_path, 'w') as f:
        json.dump(cam_para, f)


new_cam_para = generate_new_data_set('ff', 'hd', 'xavci', 422, 10, 25, 'mxf', 112)
write_to_json('fx6', new_cam_para)