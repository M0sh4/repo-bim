from app.auth.application.auth_services import AuthService
from app.infraestructure.adapters.lambda_adapter import LambdaAdapter
import app.shared.config as cfg


ambiente = "uat"
conexion = "api"
auth_services = AuthService(ambiente, conexion,'')

class peticionTest():
    
	def ejecutar(self):
		request_comviva = {
			'api_name': 'api_ums_user_account_creation', 
			'Authorization': 'Bearer',
			'data': 
			{
				'source': 'MOBILE', 
				'registrationType': 'ADM_ASSTD_REGISTRATION', 
				'userInformation': 
				{
					'basicInformation': 
					{
						'loginIdentifiers': 
							[
								{
									'type': 'KYCID', 
									'value': '72978063'
								}
							], 
						'paymentHandleIdentifiers': 
							[
								{
									'type': 'MSISDN', 
									'value': '51957457147'
								}
							], 
						'preferredLanguage': 'es', 
						'mobileNumber': '51957457147', 
						'attr1': 'claro', 
						'remarks': 'CUSTOMER_SELF_REGISTRATION'
					}, 
					'workspaceInformation': 
					{
						'workspace': 'SUBSCRIBER', 
						'categoryName': 'Final User', 
						'categoryCode': 'SUBS'
					}
				}, 
				'kycs': 
				[
					{
						'kycIdType': 'DNI', 
						'kycIdValue': '72978063', 
						'kycIdIssueDate': '2019-10-07', 
						'isPrimaryKYCId': 'Yes'
					}
				], 
				'profileDetails': 
					{
						'authProfile': 'SubsDefault', 
						'marketingProfile': 'MKPFGCRANDES04', 
						'regulatoryProfile': 'FULL_KYC', 
						'securityProfile': 'SP.23742842818527'
					}
			}
		}


		lambda_adapter = LambdaAdapter(cfg.ambiente[str(ambiente)], request_comviva,'admin', 100, "","",ambiente, conexion,'')
		result = lambda_adapter.peticion_mobiquity()

		print(result)

if __name__ == "__main__":
	ejecutar_test = peticionTest()
	ejecutar_test.ejecutar()