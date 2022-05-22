import sys


def recording_time(bitrate, capacity):
    """
    Calculate how long the camera can record based on a certain bit rate
    and card capacity.
    """
    time = round(capacity * 1000 * 8 / bitrate / 60)
    print(f"Can record up to {time} minutes (theoretically).")


if len(sys.argv) < 3:
    print('Usage: recording_time_calc.py [bitrate] [capacity]')
    sys.exit()
else:
    bitrate = int(sys.argv[1])
    capacity = int(sys.argv[2])
    recording_time(bitrate, capacity)