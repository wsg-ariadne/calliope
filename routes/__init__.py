from typing import TYPE_CHECKING
from .classify import bp_classify
if TYPE_CHECKING:
    from flask import Flask


def install_routes(app: 'Flask') -> None:
    url_prefix = '/classify'
    app.register_blueprint(bp_classify, url_prefix=url_prefix)
