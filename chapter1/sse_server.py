import tornado.ioloop
import tornado.web
from asyncio import sleep

push_flag = True

class ServerSentEvent(tornado.web.RequestHandler):
    def __init__(self,*args,**kwags):
        super(ServerSentEvent,self).__init__(*args,**kwags)
        self.set_header('Content-Type', 'text/event-stream')
        self.set_header('Access-Control-Allow-Origin', "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        # 请求方式
        self.set_header("Access-Control-Allow-Methods", "*")

    def on_finish(self) -> None:
        print("close connection")
        super().on_finish()

    async def get(self):
        print("connection")
        while True:
            if push_flag:
                print("begin")
                self.write("event: message\n");
                self.write("data:" + "push data" + "\n\n");
                self.flush()
                await sleep(2)


def make_app():
    return tornado.web.Application([
        (r"/sse/data/",ServerSentEvent),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("sse begin")
    tornado.ioloop.IOLoop.current().start()