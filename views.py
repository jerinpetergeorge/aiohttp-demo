import json
from aiohttp import web
from functions import random_character_generator, random_integer_generator

routes = web.RouteTableDef()


@routes.get('/')
async def stream_file_download(request):
    request_payload = request.query
    filename = request_payload.get('filename', 'sample_file')
    headers = {'Content-Disposition': f'attachment; filename="{filename}.json"', 'Content-Type': 'text/json'}
    resp = web.StreamResponse(status=200, reason='OK', headers=headers)
    await resp.prepare(request)
    for _ in range(100000):
        await resp.write(random_character_generator().encode())
        await resp.write(random_integer_generator().encode())
    return resp


app = web.Application()
app.add_routes(routes)
web.run_app(app)
