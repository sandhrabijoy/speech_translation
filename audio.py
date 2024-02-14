import wave
obj=wave.open("audio.wav","rb")
print("Number of channels",obj.getnchannels())
print("Sample width ",obj.getsampwidth())
print("Frame rate",obj.getframerate())
print("Number of frames",obj.getnframes())
print("Parameters",obj.getparams())

t_audio=obj.getnframes()/obj.getframerate()
print(t_audio)