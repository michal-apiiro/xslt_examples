import picoweb
import uasyncio as asyncio
import machine
import esp32

app = picoweb.WebApp(__name__)

@app.route("/<route>")
async def dump(req, resp):
    LOG.info("{} {}<>{}".format(req.method, req.path, req.qs))
    LOG.info("{}".format(req))

    LOG.info("Headers {}".format(req.headers))
    if req.method == "POST":
        pass

@app.route("/<route>",methods=['GET'])
async def stats(req, resp):
    result = {}
    await _json_response(resp, result,headers=corsHeader)