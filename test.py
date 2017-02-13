from sanic.response import text, json


async def handler1(request):
    return text('OK')


async def handler2(request, name):
    return text('Folder - {}'.format(name))


async def person_handler2(request, name):
    return text('Person - {}'.format(name))
