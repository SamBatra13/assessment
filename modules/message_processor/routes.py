from flask import Blueprint
from flask_restful import Api
from modules.message_processor.controller.message_processor import GenerateMessage, ProcessFunction


message_processor_blueprint = Blueprint('message_process', __name__, url_prefix='/process_message')
message_processor_api = Api(message_processor_blueprint)
message_processor_api.add_resource(GenerateMessage, '/generate_message')
message_processor_api.add_resource(ProcessFunction, '/process_function')