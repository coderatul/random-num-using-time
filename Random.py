import datetime
import pytz  # Required library for time zone support

def randomnum(time_zone):
    # Getting the current time in the specified time zone
    time_now = datetime.datetime.now(pytz.timezone(time_zone))
    
    # Getting time in terms of microseconds
    random_seed = time_now.microsecond
    
    # An equation which returns a number between 0 and 10
    seed = random_seed * 8 % 11
    
    # Making random number somewhat unpredictable
    random_micro_secs = []
    for i in range(seed):
        random_micro_secs.append(time_now.second**seed)
    
    seed_2 = sum(random_micro_secs)
    
    # Generating the final random number
    truly_random_num = (seed_2 * 8 % 11)
    
    return truly_random_num

# Example usage
time_zone = 'America/New_York'  # Specify the desired time zone
random_number = randomnum(time_zone)
print(random_number)
