import sys


# Functions
def recording_time(bitrate, capacity):
    """
    Calculate how long the camera can record based on a certain bit rate
    and card capacity.
    """
    time = round(capacity * 1000 * 8 / bitrate / 60)
    print(f"Can record up to {time} minutes (theoretically).")


def get_bitrate(camera, resolution, frame_rate):
    """Get bitrate from database and return"""
    if camera == 'fx6':
        index = f"{resolution}_xavc-i_422_10_{str(frame_rate)}"
        bitrate = fx6[index]
        return bitrate
    elif camera == 'fx3':
        index = f"{resolution}_xavc-s-i_422_10_{str(frame_rate)}"
        bitrate = fx3[index]
        return bitrate


# Data
fx6 = {
    'uhd_xavc-i_422_10_50': 500,
    'uhd_xavc-i_422_10_25': 250,
    'hd_xavc-i_422_10_50': 222,
    'hd_xavc-i_422_10_25': 112
}

fx3 = {
    'uhd_xavc-s-i_422_10_50': 500,
    'uhd_xavc-s-i_422_10_25': 250,
    'uhd_xavc-s_422_10_50': 200,
    'uhd_xavc-s_422_10_25': 140
}

cam_list = [fx6, fx3]

_1 = {
    'resolution': 'uhd',
    'codec': 'xavc-i',
    'chroma subsampling': 422,
    'bit depth': 10,
    'frame rate': 50,
    'bitrate': 500,
}

_2 = {
    'resolution': 'uhd',
    'codec': 'xavc-i',
    'chroma subsampling': 422,
    'bit depth': 10,
    'frame rate': 25,
    'bitrate': 250,
}

fx6 = [_1, _2]

# # for command line usage
# if len(sys.argv) < 4:
#     sys.exit()
#     print('Usage: recording_time_calc.py [camera] [resolution] [frame rate] [card capacity]')

# sys.argv = ['', 'fx3', 'uhd', 50, 80]

cam = sys.argv[1]
res = str(sys.argv[2])
fr = sys.argv[3]
capa = int(sys.argv[4])

br = get_bitrate(cam, res, fr)
recording_time(br, capa)