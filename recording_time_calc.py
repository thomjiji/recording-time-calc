import sys


def recording_time(bitrate, capacity):
    """
    Calculate how long the camera can record based on a certain bit rate
    and card capacity.
    """
    time = round(capacity * 1000 * 8 / bitrate / 60)
    print(f"Can record up to {time} minutes (theoretically).")


def looking_for_bitrate(camera, resolution, frame_rate):
    # camera = sys.argv[1]
    # resolution = sys.argv[2]
    # frame_rate = sys.argv[3]
    frame_rate = str(frame_rate)

    if camera == 'fx6':
        x = f"{resolution}_xavc-i_422_10_{frame_rate}"
        print(fx6[x])

    # if camera not in cam:
    #     print("please update your database.")
    # elif camera == 'fx6':
    #     x = f"{resolution}_xavc-i_422_10_{frame_rate}"
    #     print(x)
    # elif camera == 'fx3':
    #     bitrate = fx3[f"{resolution}_xavc-s-i_422_10_{frame_rate}"]
    #     print(bitrate)


sys.argv = ['', 'fx6', 'uhd', '25', '80']

# Data
fx6 = {'uhd_xavc-i_422_10_50': 500,
       'uhd_xavc-i_422_10_25': 250,
       'hd_xavc-i_422_10_50': 222,
       'hd_xavc-i_422_10_25': 112}

fx3 = {'uhd_xavc-s-i_422_10_50': 500,
       'uhd_xavc-s-i_422_10_25': 250,
       # 'uhd_xavc-s_422_10_50': 200,
       # 'uhd_xavc-s_422_10_25': 140
       }

cam = [fx6, fx3]
print(cam[0])

# # for command line usage
# if len(sys.argv) < 4:
#     print('Usage: recording_time_calc.py [camera] [resolution] [frame rate] [card capacity]')
#     sys.exit()


# camera = input("Please enter camera: ")
# resolution = input("Please enter resolution: ")
# frame_rate = input("Please enter frame rate: ")
# capacity = int(input("please enter card capacity: "))
#
# bitrate = fx6[f"{resolution}_xavc-i_422_10_{frame_rate}"]
#
# recording_time(bitrate, capacity)