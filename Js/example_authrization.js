const router = require('express').Router();

router.route(['/route_path', '/route_something']).get((req, res) => {
	if (req.headers.authorization) {
		const authorization = req.headers.authorization.replace('', '');
    }
});

