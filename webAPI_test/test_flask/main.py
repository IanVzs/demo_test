from gevent import monkey
monkey.patch_all()
#--------------------------------#
import sys
import gevent
from gevent import pywsgi


from app import app, TESTAPI

def exception_callback(g):
    pass

app.register_blueprint(TESTAPI)
if __name__ == '__main__':
    server = pywsgi.WSGIServer(("0.0.0.0", 8979), app)
    sys.stderr.write("server started %s:%s\n" % ("0.0.0.0", 8979))
    main_task = gevent.spawn(server.serve_forever)
    main_task.link_exception(exception_callback)
    all_tasks = [main_task]
    gevent.joinall(all_tasks)
