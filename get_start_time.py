
def convert_minutes(time):
    '''
    Time is in format hh:mm
    return integer of minutes
    '''
    return int(time.split(':')[0])*60 + int(time.split(':')[1]) - 9*60

def convert_hhmm(minutes):
    '''
    minutes is integer
    returns string in hh:mm format
    '''
    hh, mm = divmod(minutes, 60)
    return '{:02d}:{:02d}'.format(hh+9,mm)


def quarter_interval(minutes):
    '''
    Returns the integer of quarter
    '''
    idx, rem = divmod(minutes,1)
    if rem > 0:
        idx += 1
    return idx

def meeting_to_index(meeting):
    return quarter_interval(convert_minutes(meeting[0])), quarter_interval(convert_minutes(meeting[1]))

def index_to_meeting(idx):
    minutes = 1*idx
    return convert_hhmm(minutes)

def get_start_time(schedules, duration):
    # list of number of quarters in a business day
    final_quarter = quarter_interval(convert_minutes('19:00'))
    business_day = [0 for ii in range(final_quarter)]
    # convert time in intervals of 15
    
    # parse each persons schedule
    for schedule in schedules:
        for meeting in schedule:
            start, end = quarter_interval(convert_minutes(meeting[0])), quarter_interval(convert_minutes(meeting[1]))
            for idx in range(start,end,1):
                business_day[idx] += 1
    duration = quarter_interval(duration)
    start_slot = None
    
    free_slot = None
    for idx,slot in enumerate(business_day):
         if slot == 0 and start_slot is None:
             start_slot = idx
             free_slot = 1
         elif slot == 0 and start_slot is not None:
             free_slot += 1
             if free_slot == duration:
                 return index_to_meeting(start_slot)
         else:
             start_slot = None
    return None
             


duration = 38
schedules = [
        [['10:07', '10:39'], ['10:41', '11:03'], ['12:21', '12:22'], ['15:49', '16:11'], ['17:29', '17:54']], 
        [['09:41', '09:57'], ['10:03', '10:14'], ['10:32', '10:39'], ['10:56', '11:17'], ['11:23', '11:41'], ['11:59', '12:03'], ['12:28', '12:45'], ['17:19', '17:27'], ['18:56', '18:57']], 
        [['09:48', '12:26'], ['15:41', '15:59'], ['18:50', '18:57']], 
        [['09:37', '11:19'], ['11:27', '13:37'], ['16:29', '17:41']], 
        [['11:21', '12:42'], ['12:51', '13:20'], ['17:51', '17:53'], ['18:07', '18:11']]]


print(get_start_time(schedules,duration))

