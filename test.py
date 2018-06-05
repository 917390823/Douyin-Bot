import wda
import time
c = wda.Client()
s = c.session()

# s.tap_hold(700, 600, 0.01)
# time.sleep(0.5)
s.swipe(375, 1067, 375, 367, 0.01)
time.sleep(0.5)
s.close()