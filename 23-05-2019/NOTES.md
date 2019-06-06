# Notes

1.  You do not have to check the last number; if there was a pair you would have already found it by then.

2.  Notice that the membership check (which is quite costly in lists) is optimized since it considers the slice ```numbers[i+1:]``` only. The previous numbers have been checked already. A positive side-effect of the slicing is that the existence of one 4 in the list, does not give a pair for a target value of ```8```.

3. This is an excellent setup to explain the miss-understood and often confusing use of ```else``` in ```for```-loops. The ```else``` triggers only if the loop was not abruptly ended by a ```break```.