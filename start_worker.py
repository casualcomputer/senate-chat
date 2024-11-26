from rq import Worker, Queue
from redis import Redis

if __name__ == "__main__":
    redis_conn = Redis()  # Connect to Redis server
    worker = Worker(Queue(connection=redis_conn))  # Create a worker for the default queue
    print("Worker started, processing jobs...")
    worker.work()
