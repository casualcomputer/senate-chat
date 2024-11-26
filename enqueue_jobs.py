# enqueue_jobs.py
from redis import Redis
from rq import Queue
import os
from tasks import transcribe_chunk_job  # Import the job function

def enqueue_transcription_jobs(chunk_dir, redis_conn, model_path="small"):
    """
    Enqueues transcription jobs for each audio chunk in the Redis queue.
    Args:
        chunk_dir (str): Directory containing audio chunks.
        redis_conn: Redis connection object.
        model_path (str): Model size to use for transcription.
    """
    q = Queue(connection=redis_conn)
    chunk_files = [os.path.join(chunk_dir, f) for f in os.listdir(chunk_dir) if f.endswith(".mp3")]
    print(f"Found {len(chunk_files)} chunks for transcription.")

    for chunk_path in chunk_files:
        q.enqueue(transcribe_chunk_job, chunk_path, model_path)
        print(f"Enqueued {chunk_path}")

if __name__ == "__main__":
    redis_conn = Redis()  # Connect to Redis server
    chunk_dir = "./chunks"  # Directory containing audio chunks
    enqueue_transcription_jobs(chunk_dir, redis_conn)