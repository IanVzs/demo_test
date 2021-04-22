import os
import logging
from multiprocessing import Process, Pool

from tornado.options import define, options
from {xxx} import common, setting

setting.define_options()
options.parse_command_line(final=False)
if options.conf_path and os.path.exists(options.conf_path):
    options.parse_config_file(options.conf_path, final=False)
options.parse_command_line(final=True)

options.log_path = options.log_path or "logs/delayer.log"
options.log_level = logging.DEBUG

common.set_log()
# define('trace_format', default=0)
from delay_event import delay_event, config as DLY_CFG


def run(name=''):
    delayer = delay_event.Delayer(name=name)
    delayer.run()


if __name__ == "__main__":
    list_names = [DLY_CFG.CHAT_TIMEOUT, DLY_CFG.CHAT_MSG]
    # # region Process实现
    # list_p = []
    # for i in list_names:
    #     p = Process(target=run, args=(i, ))
    #     p.start()
    #     list_p.append(p)
    # for p in list_p:
    #     p.join()
    # #endregion

    # region Pool实现
    pool = Pool(processes=len(list_names))
    for i in list_names:
        pool.apply_async(run, (i, ))
    pool.close()
    pool.join()
    #endregion
