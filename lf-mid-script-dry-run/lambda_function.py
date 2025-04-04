from main import DryRunMain
import aws_xray_sdk.core
import asyncio

aws_xray_sdk.core.patch_all()

def lambda_handler(event, context):
    custom_body = event.get('body', '{}')
    proceso_dr = custom_body['proceso_dr']
    print(f"Inicio de ejecución en AWS Lambda. {event}")
    try:
        if(proceso_dr == 'proceso_stress'):
            dry_run_main = DryRunMain(event_data=event)
            result = asyncio.run(dry_run_main.pre_dryrun_main())
            return {"statusCode": result["response_mob"]["statusCode"], "body": f"{str(result)}"}
        elif(proceso_dr == 'proceso_dryrun'):
            dry_run_main = DryRunMain(event_data=event)
            asyncio.run(dry_run_main.pre_dryrun_main())
            return {"statusCode": 200, "body": f"Ejecución finalizada correctamente en DR."}
    except Exception as e:
        print(f"Error durante la ejecución en AWS Lambda: {e}")
        return {"statusCode": 500, "body": f"Error DR: {str(e)}"}