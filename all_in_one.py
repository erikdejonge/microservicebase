# coding=utf-8
import logging
import asyncio
import api_hour
import aiohttp.web
from aiohttp.web import Response

logging.basicConfig(level=logging.INFO)  # enable logging for api_hour


class Container(api_hour.Container):

    def __init__(self, *args, **kwargs):
        """
        @type args: tuple
        @type kwargs: dict
        @return: None
        """
        super().__init__(*args, **kwargs)

        # Declare HTTP server
        self.servers['http'] = aiohttp.web.Application(loop=kwargs['loop'])
        self.servers['http'].ah_container = self  # keep a reference in HTTP server to Container

        # Define HTTP routes
        self.servers['http'].router.add_route('GET',
                                              '/',
                                              self.index)

    # A HTTP handler example
    # More documentation: http://aiohttp.readthedocs.org/en/latest/web.html#handler

    @asyncio.coroutine
    def index(self, request):
        """
        @type request: HttpRequest, django.core.handlers.wsgi.WSGIRequest
        @return: None
        """
        message = 'Hello World !'
        return Response(text=message)

    # Container methods

    @asyncio.coroutine
    def start(self):
        """
        start
        """

        # A coroutine called when the Container is started
        yield from super().start()

    @asyncio.coroutine
    def stop(self):
        """
        stop
        """

        # A coroutine called when the Container is stopped
        yield from super().stop()

    def make_servers(self):
        """
        make_servers
        """

        # This method is used by api_hour command line to bind your HTTP server on socket
        return [self.servers['http'].make_handler(logger=self.worker.log,
                                                  keep_alive=self.worker.cfg.keepalive,
                                                  access_log=self.worker.log.access_log,
                                                  access_log_format=self.worker.cfg.access_log_format)]
