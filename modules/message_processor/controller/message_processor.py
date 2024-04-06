from flask_restful import Resource, request
from modules.message_processor.services.messsage_processor import MessageProcessor, MessageProcessFactory


class GenerateMessage(Resource):

    def post(self):
        try:
            data = request.get_json()
            if 'message' in data:
                message = data['message']
                processor = MessageProcessor()
                processor.push_message(message)
        except Exception as e:
            print("Exception in GenerateMessage: ", e)

class ProcessFunction(Resource):

    def post(self):
        try:
            data = request.get_json()
            func_name = data.get('func_name')
            num_messages = data.get('num_messages')
            processor = MessageProcessFactory()
            obj = processor.create_message_processor(num_workers=2, use_multiprocessing=False)
            obj.process_stream(func_name, num_messages)
        except Exception as e:
            print("Exception in ProcessFunction: ", e)