TIME_MICROSEKUNDS = 0

_ticks = 0

def sleep_us(time):
  global TIME_MICROSEKUNDS
  TIME_MICROSEKUNDS = TIME_MICROSEKUNDS + time


def ticks_ms():
   return _ticks

def ticks_add(time, delta):
  return time + delta

def time_ms():
  return TIME_MICROSEKUNDS

def ticks_diff(delta, time):
  return delta - TIME_MICROSEKUNDS
