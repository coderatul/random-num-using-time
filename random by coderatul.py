#importing datetime module 
import datetime #inbuilt module
time_now  = datetime.datetime.now()
#getting time in terms of microseconds
random_seed = time_now.microsecond 
 # an equation which returns a number between 0 and 10 & takes an integer as a parameter 
seed =  random_seed * 8 % 11
#making random number somewhat unpredictable !!!
random_micro_secs = []
for i in range(seed):
  random_micro_secs.append(time_now.second**seed)
seed_2 = sum(random_micro_secs)
#generating final random number 
truely_random_num=(seed_2 * 8 % 11)
print(truely_random_num)

  

  
  
  

  
