from ToQueue import app,db
from ToQueue.models import Task

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'Task':Task}