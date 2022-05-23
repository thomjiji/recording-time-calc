import json
import sys


def recording_time(bitrate, capacity):
    """
    Calculate how long the camera can record based on a certain bit rate
    and card capacity.
    """
    time = round(capacity * 1000 * 8 / bitrate / 60)
    print(f"Can record up to {time} minutes (theoretically).")


def get_bitrate(camera,
                sensor_mode,
                resolution,
                codec,
                chroma_subsampling,
                bit_depth,
                frame_rate,
                file_format):
    """Get bitrate from database and return."""
    filename = f"{camera}_database.json"
    with open(filename, 'r') as f:
        x = json.load(f)
        for i in x:
            if i['sensor mode'] == sensor_mode:
                if i['resolution'] == resolution:
                    if i['codec'] == codec:
                        if i['chroma subsampling'] == chroma_subsampling:
                            if i['bit depth'] == bit_depth:
                                if i['frame rate'] == frame_rate:
                                    if i['file format'] == file_format:
                                        print(i['bitrate'])
                                    else:
                                        print("file format is not matching.")
                                else:
                                    print("frame rate is not matching.")
                            else:
                                print("bit depth is not matching.")
                        else:
                            print("chroma subsampling is not matching.")
                    else:
                        print("codec is not matching.")
                else:
                    print("resolution is not matching.")
            else:
                print("sensor mode is note matching.")

    # if camera == 'fx6':
    #     index = f"{resolution}_xavc-i_422_10_{str(frame_rate)}"
    #     bitrate = fx6[index]
    #     return bitrate
    # elif camera == 'fx3':
    #     index = f"{resolution}_xavc-s-i_422_10_{str(frame_rate)}"
    #     bitrate = fx3[index]
    #     return bitrate


# Data (legacy)
fx6 = {
    'uhd_xavc-i_422_10_50': 500,
    'uhd_xavc-i_422_10_25': 250,
    'hd_xavc-i_422_10_50': 222,
    'hd_xavc-i_422_10_25': 112,
}

fx3 = {
    'uhd_xavc-s-i_422_10_50': 500,
    'uhd_xavc-s-i_422_10_25': 250,
    'uhd_xavc-s_422_10_50': 200,
    'uhd_xavc-s_422_10_25': 140,
}

cam_list = [fx6, fx3]

# # for command line usage
# if len(sys.argv) < 4:
#     sys.exit()
#     print('Usage: recording_time_calc.py
#     [camera] [sensor mode] [resolution] [chroma subsampling] [frame rate] [file format] [card capacity]')

sys.argv = ['', 'fx3', 'uhd', 50, 80]

cam = sys.argv[1]
res = str(sys.argv[2])
fr = sys.argv[3]
capa = int(sys.argv[4])

# br = get_bitrate(cam, res, fr)
# recording_time(br, capa)
get_bitrate('fx6', 'ff', 'uhd', 'xavci', 422, 10, 25, 'mxf')