import queue
import threading
import multiprocessing
import time
from flask import Flask, jsonify

# Message Processor Framework Class


class MessageProcessorBase:
    def process_message(self, message):
        raise NotImplementedError()
        # Process the message using the specified processing function
    
class MessageProcessor(MessageProcessorBase):
    def __init__(self, num_workers=1, use_multiprocessing=False):
        self.message_queue = queue.Queue()
        self.num_workers = num_workers
        self.use_multiprocessing = use_multiprocessing

    def process_message(self, message, process_func):
        # Process the message using the specified processing function
        result = process_func(message)
        print(f"Processed Message: {message} -> {result}")

    def worker(self, process_func):
        # Worker function that continuously processes messages from the queue
        while True:
            message = self.message_queue.get()
            if message is None:
                break
            self.process_message(message, process_func)
            self.message_queue.task_done()

    def start_workers(self, process_func):
        workers = [
            multiprocessing.Process(target=self.worker, args=(process_func,))
            if self.use_multiprocessing
            else threading.Thread(target=self.worker, args=(process_func,))
            for _ in range(self.num_workers)
        ]
        for worker in workers:
            worker.start()
        return workers

    def process_stream(self, process_func, stream_func, num_messages=10):
        # Entry point to start processing messages from a stream
        workers = self.start_workers(process_func)

        for _ in range(num_messages):
            message = stream_func() # Generate a message from the stream
            self.message_queue.put(message)

        # Block until all messages are processed
        self.message_queue.join()

        # Stop workers by sending None to the queue
        for _ in range(self.num_workers):
            self.message_queue.put(None)

        # Wait for all workers to complete
        for worker in workers:
            worker.join()


class MessageProcessFactory:
    @staticmethod
    def create_message_processor(num_workers=1, use_multiprocessing=False):
        return MessageProcessor(num_workers, use_multiprocessing)

# Example: Processing Functions
def process_function_1(message):
    # Example processing function 1
    return message.upper()

def process_function_2(message):
    # Example processing function 2
    return message[::-1]

app = Flask(__name__)

processor = MessageProcessFactory.create_message_processor(num_workers=2, use_multiprocessing=False)

@app.route("/process_function_1")
def process_function_1_route():
    processor.process_stream(process_function_1, stream_messages, num_messages=5)
    return jsonify({"message": "Processing function 1 completed"})

@app.route("/process_function_2")
def process_function_2_route():
    processor.process_stream(process_function_2, stream_messages, num_messages=5)
    return jsonify({"message": "Processing function 2 completed"})

def stream_messages():
    return str(time.time())

if __name__ == "__main__":
    app.run(debug=True)
