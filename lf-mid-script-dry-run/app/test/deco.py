import base64

base64_message = "NTE5ODI4ODU5NDI6MTIxMjEy"
base64_bytes = base64_message.encode('utf-8')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('utf-8')

print(f"{message}")
# e6f19068-84c4-447b-b32a-b9a9960aaabb  12345679
#51977570979:280985
#51977570979:280985
#51912701326:260790
#51938751343:161205
#51970934229:135790


#51977389624:040181