from cryptography.fernet import Fernet
import os.path
import base64

balls = 'what is up'
ballsEncoded = base64.b64encode(balls.encode('utf-8'))
print(ballsEncoded)


ballsDecoded = base64.b64decode(ballsEncoded.decode('utf-8'))
encoding = 'utf-8'
ballsTREALLYDECODED = ballsDecoded.decode(encoding)
print(ballsTREALLYDECODED)
