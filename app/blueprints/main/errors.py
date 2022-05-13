from flask import current_app as app

@app.errorhandler(404)
def not_found_error(error):
    return "What you are looking for isn't here on our site, please try again."

@app.errorhandler(500)
def internal_server(error):
    return "There seems to be a problem with our server. We are diligently working on fixing the issue."

