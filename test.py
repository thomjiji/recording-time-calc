import sys

# Data
fx6 = [['uhd', 'xavc-i', 422, 10, 50, 500],
       ['uhd', 'xavc-i', 422, 10, 25, 250],
       ['hd', 'xavc-i', 422, 10, 50, 222],
       ['hd', 'xavc-i', 422, 10, 25, 112]]

fx3 = [['uhd', 'xavc-s-i', 422, 10, 50, 500],
       ['uhd', 'xavc-s-i', 422, 10, 25, 250],
       ['uhd', 'xavc-s', 422, 10, 50, 200],
       ['uhd', 'xavc-s', 422, 10, 25, 140]]

cam = [fx6, fx3]


# Functions
def bitrate(res, camera, frame_rate):
    if camera in cam:
        for list in camera:
            if list[0] == res:
                if list[-2] == frame_rate:
                    return list[-1]
    else:
        print("This camera is not in database.")


def recording_time(bitrate, capacity):
    """
    Calculate how long the camera can record based on a certain bit rate
    and card capacity.
    """
    time = round(capacity * 1000 * 8 / bitrate / 60)
    print(f"Can record up to {time} minutes (theoretically).")


# for command line usage
# if len(sys.argv) < 5:
#     print('Usage: recording_time_calc.py [camera] [resolution] [frame rate] [card capacity]')
#     sys.exit()

bitrate = bitrate(sys.argv[3], sys.argv[2], sys.argv[4])

capacity = int(sys.argv[4])
recording_time(bitrate, capacity)