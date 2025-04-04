import boto3
import json
import boto3.session

payload = {"code":200, "message": '''	
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>            <ns2:cashinrequest xmlns:ns2="http://www.ericsson.com/em/emm/financial/v1_0">                <sendingfri>FRI:BNAPWVIRTUAL157/USER</sendingfri>                <receivingfri>FRI:51902195929/MSISDN</receivingfri>                <amount>1.00</amount>                <sendernote>7665230520241113111419090641</sendernote>                <receivermessage>7665230520241113111419090641</receivermessage>            </ns2:cashinrequest>'''}

payload2 = str(payload)

print(payload2)