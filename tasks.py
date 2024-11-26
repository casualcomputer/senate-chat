#tasks.py
import os
from whisper import load_model

def transcribe_chunk_job(chunk_path, model_path="small"):
    """
    Transcribes a single audio chunk.
    Args:
        chunk_path (str): Path to the audio chunk file.
        model_path (str): Model size to load (e.g., "small", "base").
    Returns:
        tuple: Chunk file name and transcription text.
    """
    try:
        model = load_model(model_path)
        result = model.transcribe(chunk_path)
        return os.path.basename(chunk_path), result["text"]
    except Exception as e:
        return os.path.basename(chunk_path), f"Error: {str(e)}"


import os
from whisper import load_model

def transcribe_chunk_job(chunk_path, model_path="small"):
    try:
        print(f"Starting transcription for {chunk_path} with model {model_path}...")
        model = load_model(model_path)
        result = model.transcribe(chunk_path)
        transcription_text = result["text"]
        print(transcription_text)
        
        # Save transcription
        chunk_name = os.path.basename(chunk_path)
        output_file = f"./transcriptions/{chunk_name}.txt"
        os.makedirs("./transcriptions", exist_ok=True)
        with open(output_file, "w") as f:
            f.write(transcription_text)

        print(f"Transcription for {chunk_name} saved to {output_file}.")
        return chunk_name, transcription_text
    except Exception as e:
        print(f"Error processing {chunk_path}: {str(e)}")
        return os.path.basename(chunk_path), f"Error: {str(e)}"


