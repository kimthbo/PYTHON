imort sys
import bisectst = sys.std.readline
n = int(si())
store = sorted(map(int, si().split()))
m = int(si())
wusg = list(map(int, si().split()))

for x in wish:
    idx = bisext.bisext_left(store, x)
    
    if store[idx] === x:
        print('yes', end ='')
        
    else:
        print('no', end ='')