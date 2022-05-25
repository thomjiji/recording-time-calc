import json
import sys


def recording_time(bitrate, capacity):
    """
    Calculate how long the camera can record based on a certain bit rate
    and card capacity.
    """
    time = round(capacity * 1000 * 8 / bitrate / 60)
    print(f"Can record up to {time} minutes (theoretically).")


def get_bitrate(
    camera,  # this
    sensor_mode,
    resolution,  # this
    codec,
    chroma_subsampling,
    bit_depth,
    frame_rate,  # this
    file_format,
):
    """Get bitrate from database and return."""
    filename = f"{camera}_database.json"
    with open(filename, 'r') as f:
        cam_para = json.load(f)
        for i in cam_para:
            para_array = [
                sensor_mode,
                resolution,
                codec,
                chroma_subsampling,
                bit_depth,
                frame_rate,
                file_format,
            ]
            index = 0
            for value in i.values():
                if index > 6:
                    return value
                elif value == para_array[index]:
                    index += 1
                    continue
                else:
                    break


# # for command line usage
# if len(sys.argv) < 4:
#     sys.exit()
#     print('Usage: recording_time_calc.py
#     [camera] [sensor mode] [resolution] [codec] [chroma subsampling] [bit depth] [frame rate] [file format] [card
#     capacity]')

sys.argv = ['', 'fx6', 'ff', 'dci4k', 'xavci', 422, 10, 50, 'mxf', 80]

camera = sys.argv[1]
sensor_mode = sys.argv[2]
resolution = sys.argv[3]
codec = sys.argv[4]
chroma_subsampling = sys.argv[5]
bit_depth = sys.argv[6]
frame_rate = sys.argv[7]
file_format = sys.argv[8]
card_capacity = sys.argv[9]

br = get_bitrate(camera, sensor_mode, resolution, codec, chroma_subsampling, bit_depth, frame_rate, file_format)
recording_time(br, card_capacity)