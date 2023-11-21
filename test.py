import whisper_timestamped as whisper
import json


model = whisper.load_model("tiny", device="cpu")

def transcribe(audio_file):
    audio = whisper.load_audio(audio_file)
    result = whisper.transcribe(model, audio, language="en")
    return result


__all__ = ["transcribe"]
# f = open("l2.json", "a")
# f.write(json.dumps(result, indent = 2, ensure_ascii = False))
# f.close()

# file_path = "Try Orchestrator workflow - Journey-Don't_Stop_Believing-Multitrack--Vocals Music.wav"
# print(transcribe(file_path))