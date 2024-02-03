"""
Basic usage of PowerProfiler
"""
import time
from power_profiler import PowerProfiler

powerProfilerInstance = PowerProfiler()
powerProfilerInstance.start_measuring()

time.sleep(5)

powerProfilerInstance.stop_measuring()

averageCurrentMa = powerProfilerInstance.get_average_current_mA()
print(f'averageCurrentMa={averageCurrentMa}')