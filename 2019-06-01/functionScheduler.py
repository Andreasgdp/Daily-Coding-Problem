import time

def test():
  print('Hello World!')

def scheduler(functionName, milliseconds): # note 1
  time.sleep(milliseconds/1000)
  eval('f()'.replace('f', functionName)) # note 2T

scheduler('test', 3000)

# note 3