import base64

message = 'VIRTUALINTEROP2:Com@135@18'
message_bytes = message.encode('utf-8')
message_bytes =  base64.b64encode(message_bytes)

# base64_message = "MzMzNzc3"
# base64_bytes = base64_message.encode('utf-8')
# message_bytes = base64.b64decode(base64_bytes)
# message = message_bytes.decode('utf-8')  MDc4MDE4MDk= NTE5ODkzMzEyNDA=

print(f"{message_bytes}")