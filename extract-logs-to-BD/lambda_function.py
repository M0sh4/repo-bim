import lf_mdw_api_sender_xml_awspdp
import lf_mdw_api_sender_awspdp
import api_sender_PROD_awspdp
import lf_mdw_api_sender_awspdp1
import lf_mdw_api_sender_pdp_ewp_xml_ms
import lf_mdw_api_sender_xml_aws_bimer
import lf_mdw_api_sender_xml_aws_usuariofinal
import lf_mdw_api_sender_xml_fbs_usuariofinal
import lf_mdw_apisendercuentadni_apisendercuentadni
import prod_api_sender_awspdp
import prod_sender_awspdp
import cashin_kasnet
import cashin_prod
import ci_co_r_fullcarga
import pago_credito_fcompartamos
import r_e_sin_tarjeta

def lambda_handler(event, context):
    if event['lambda'] == 'lf_mdw_api_sender_xml_awspdp':
        lf_mdw_api_sender_xml_awspdp.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'lf_mdw_api_sender_awspdp':
        lf_mdw_api_sender_awspdp.exec_lambda(event['manual'], event['date_extract'])
    elif event['lambda'] == 'api_sender_PROD_awspdp':
        api_sender_PROD_awspdp.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'lf_mdw_api_sender_awspdp1':
        lf_mdw_api_sender_awspdp1.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'lf_mdw_api_sender_pdp_ewp_xml_ms':
        lf_mdw_api_sender_pdp_ewp_xml_ms.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'lf_mdw_api_sender_xml_aws_bimer':
        lf_mdw_api_sender_xml_aws_bimer.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'lf_mdw_api_sender_xml_aws_usuariofinal':
        lf_mdw_api_sender_xml_aws_usuariofinal.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'lf_mdw_api_sender_xml_fbs_usuariofinal':
        lf_mdw_api_sender_xml_fbs_usuariofinal.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'lf_mdw_apisendercuentadni_apisendercuentadni':
        lf_mdw_apisendercuentadni_apisendercuentadni.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'prod_api_sender_awspdp':
        prod_api_sender_awspdp.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'prod_sender_awspdp':
        prod_sender_awspdp.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'cashin_kasnet':
        cashin_kasnet.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'cashin_prod':
        cashin_prod.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'ci_co_r_fullcarga':
        ci_co_r_fullcarga.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'pago_credito_fcompartamos':
        pago_credito_fcompartamos.exec(event['manual'], event['date_extract'])
    elif event['lambda'] == 'r_e_sin_tarjeta':
        r_e_sin_tarjeta.exec(event['manual'], event['date_extract'])