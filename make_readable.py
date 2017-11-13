def make_readable(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    seconds = seconds - minutes*60 - hours*3600
    
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

# return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)