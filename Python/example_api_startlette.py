from starlette.routing import Route,Mount

routes = [
    Route('/', homepage),
    Mount('/users', routes=users.routes),
    Mount('/auth', routes=auth.routes),
]

app = Starlette(routes=routes)