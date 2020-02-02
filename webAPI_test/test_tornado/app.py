#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import sys
import asyncio
from tornado.httpclient import AsyncHTTPClient
from tornado.options import define, options

PORT = 8011
if len(sys.argv) > 1:
    PORT = sys.argv[1]
define("port", default=PORT, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    """
    async def get(self):
        self.write('"dump": "Hello, world"')
    """

    async def get(self):
        """
        处理同时有多个网络请求的异步
        :return:
        """
        task_list = []
        for i in range(1):
            task_list.append(self.asynchronous_fetch('http://127.0.0.1:8001/nginx'))
        body = await asyncio.wait(task_list)  # 将所有异步操作的结果返回,但是是无序的,要是需要返回结果的话解析起来比较麻烦
        self.finish()
        #self.write('finished!')

    async def asynchronous_fetch(self, url):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch(url)
        print("asynchronous_fetch %s" % response.body)
        return response.body


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([(r"/", MainHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()





