# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
""""
"""
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
import Wifi
#import webrepl
#webrepl.start()
gc.collect()
Wifi.do_connect()