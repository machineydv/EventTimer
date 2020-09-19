def seconds_from_time(time: str) -> int:
    time = time.split(':')
    hour = time[0]
    minute = time[1]
    second = time[2]
    return int(int(int(hour) * 60 * 60) + int(int(minute) * 60) + int(second))

def time_from_seconds(second: int) -> str:
    minute, second = divmod(int(second), 60)
    hour, minute = divmod(int(minute), 60)
    return str(':'.join([str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2)]))
    
def second_or_time(data) -> str:
    if ':' in data:
        return 'time'
    if int(data):
        return 'second'

def twenty_four_to_twelve(time):
    shift = 'AM'
    if second_or_time(time) == 'time':
        if int(time.split(':')[0]) > 12:
            shift = 'PM'
            new_time = time_from_seconds(seconds_from_time(time) - seconds_from_time('12:00:00'))
            new_time = new_time + ' ' +  shift
            return new_time
        else:
            new_time = time + ' ' + shift
            return new_time
    else:
        time = time_from_seconds(time)
        if int(time.split(':')[0]) > 12:
            shift = 'PM'
            new_time = time_from_seconds(seconds_from_time(time) - seconds_from_time('12:00:00'))
            new_time = new_time + ' ' + shift
            return new_time
        else:
            new_time = time + ' ' + shift
            return new_time

# while True:
    # time_type = input("Enter time type: GMT(G), PACIFIC(P), KTM(K): ").strip().upper()
    # to_type = input("Enter time to change to: GMT(G), PACIFIC(P), KTM(K): ").strip().upper()
    # time = input("Enter time either in second or clock (HH:MM:SS) format: ")
    # if time_type == 'P':
        # if to_type == 'K':
            # if second_or_time(time) == 'time':
                # time = seconds_from_time(time)
            # time += pacific_to_ktm_convert
            # #time_print()
            # #print(time_from_seconds(time))
            # break
    # if time_type == 'K':
        # if to_type == 'P':
            # if second_or_time(time) == 'time':
                # time = seconds_from_time(time)
            # time -= pacific_to_ktm_convert
            # #time_print()
            # print(time_from_seconds(time))
            # break

