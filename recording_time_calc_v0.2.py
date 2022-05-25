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
        return None


# # for command line usage
# if len(sys.argv) < 4:
#     sys.exit()
#     print('Usage: recording_time_calc.py
#     [camera] [sensor mode] [resolution] [codec] [chroma subsampling] [bit depth] [frame rate] [file format] [card
#     capacity]')

sys.argv = ['', 'fx6', 'ff', 'uhd', 'xavci', 422, 10, 25, 'mxf', 160]

cam = sys.argv[1]
senmo = sys.argv[2]
res = sys.argv[3]
cdc = sys.argv[4]
chrsub = sys.argv[5]
bd = sys.argv[6]
fr = sys.argv[7]
ff = sys.argv[8]
capa = sys.argv[9]

br = get_bitrate(cam, senmo, res, cdc, chrsub, bd, fr, ff)
if not br:
    print(f"Please update your {cam}'s database.")
else:
    recording_time(br, capa)