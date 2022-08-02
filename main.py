from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

from entities import Entity
app = Flask(__name__)
api = Api(app)
CORS(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


#new coment
# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

class HelloWorld(Resource):    
     def get(self):        
         return {'hello': 'world'} 
     
class status(Resource):    
     def get(self):
        return {'data': 'Api SBC running'}
 

##
## Actually setup the Api resource routing here
##
api.add_resource(status,'/status')
api.add_resource(HelloWorld, '/')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Entity, '/entity/<text>')

# api.add_resource(Recommendation, '/recommendation/<product_id>')



if __name__ == '__main__':
    app.run(debug=True)