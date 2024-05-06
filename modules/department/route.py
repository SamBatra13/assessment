from flask import Blueprint
from flask_restful import Api
from modules.department.controllers.department import GetDepartment, AddDepartment, AssignOrDeassignDepartment

department_blueprint = Blueprint('business', __name__, url_prefix='/department')
department_api = Api(department_blueprint)


department_api.add_resource(GetDepartment, '/department_get'),
department_api.add_resource(AddDepartment, '/department_add'),
department_api.add_resource(AssignOrDeassignDepartment, '/assign_doc_to_department')
