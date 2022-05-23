import json

uhd_xavci_422_10_50 = {
    'resolution': 'uhd',
    'codec': 'xavc-i',
    'chroma subsampling': 422,
    'bit depth': 10,
    'frame rate': 50,
    'bitrate': 500,
}

uhd_xavci_422_10_25 = {
    'resolution': 'uhd',
    'codec': 'xavc-i',
    'chroma subsampling': 422,
    'bit depth': 10,
    'frame rate': 25,
    'bitrate': 250,
}

fx6 = [
    uhd_xavci_422_10_50,
    uhd_xavci_422_10_25,
]


def generate_new_data_set(resolution, codec, chroma_subsampling, bit_depth, frame_rate, bitrate):
    """generating a new set of data, return a dictionary for appending to the the camera list
    (for example fx6).
    """
    new_data_set = {}
    new_data_set.setdefault('resolution', resolution)
    new_data_set.setdefault('codec', codec)
    new_data_set.setdefault('chroma subsampling', chroma_subsampling)
    new_data_set.setdefault('bit depth', bit_depth)
    new_data_set.setdefault('frame rate', frame_rate)
    new_data_set.setdefault('bitrate', bitrate)
    return new_data_set


def add_new_data_set_to_cam_list(camera, new_data_set):
    camera.append(new_data_set)


def name_generator(new_data_set):
    name = f"{new_data_set['resolution']}_{new_data_set['codec']}_{new_data_set['chroma subsampling']}_{new_data_set['bit depth']}_{new_data_set['frame rate']}"
    return name


# filename = 'fx6_database.json'
#
# with open(filename, 'a') as f:
#     json.dump(data_added, f)


new_dict = generate_new_data_set('hd', 'xavcsi', 420, 8, 25, 122)
name = name_generator(new_dict)
fx6.append(new_dict)
for i in fx6:
    print(i, end='\n')