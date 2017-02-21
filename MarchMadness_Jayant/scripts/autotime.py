from __future__ import print_function

import time
from IPython.core.magics.execution import _format_time as format_delta


class CellTimer(object):

    """Class that implements a basic timer for printing cell execution time.

    Registered the `start` and `stop` methods with the IPython events API.
    """

    def __init__(self):
        self.start_time = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time:
            diff = time.time() - self.start_time
            if diff > 1:
                print('time: %s' % format_delta(diff))


def load_ipython_extension(ip):
    timer = CellTimer()
    ip.events.register('pre_run_cell', timer.start)
    ip.events.register('post_run_cell', timer.stop)


def unload_ipython_extension(ip):
    ip.events.unregister('pre_run_cell', timer.start)
    ip.events.unregister('post_run_cell', timer.stop)