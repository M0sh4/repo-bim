from testlink import TestlinkAPIClient
from typing import List, Dict, Optional
import requests

# Configuración
# API_URL = "http://testlink.mibim.pe/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEV_KEY = "04ded488fa8e0eddd19cb22e32092189"

# PROJECT_NAME = "QA - CALIBRACION"
# TEST_PLAN_NAME = "PRF-466"

# # Conexión
# tl = TestlinkAPIClient(API_URL, DEV_KEY)

# # Obtener proyecto por nombre
# def get_project_id_by_name(name: str) -> Optional[str]:
#     projects = tl.getProjects()
#     for p in projects:
#         if p["name"] == name:
#             return p["id"]
#     return None

# # Obtener test plan por nombre
# def get_test_plan_id_by_name(project_id: str, plan_name: str) -> Optional[str]:
#     test_plans = tl.getProjectTestPlans(project_id)
#     for plan in test_plans:
#         if plan["name"] == plan_name:
#             return plan["id"]
#     return None

# # Obtener casos de prueba del plan
# def get_test_cases_for_plan(plan_id: str) -> Dict:
#     return tl.getTestCasesForTestPlan(plan_id)

# def get_test_case_steps(tcase_id: int, version: int):
#     try:
#         tcase_info = tl.getTestCase(testcaseid=tcase_id, version=int(version))
#         print(tcase_info)
#         if isinstance(tcase_info, list):
#             tcase_info = tcase_info[0]
#         return tcase_info.get("steps", [])
#     except Exception as e:
#         print(f"⚠️ Error al obtener pasos del caso externo {external_id}: {e}")
#         return []

# # Ejecutar flujo
# project_id = get_project_id_by_name(PROJECT_NAME)
# if not project_id:
#     print(f"❌ Proyecto '{PROJECT_NAME}' no encontrado.")
#     exit()

# plan_id = get_test_plan_id_by_name(project_id, TEST_PLAN_NAME)
# if not plan_id:
#     print(f"❌ Test Plan '{TEST_PLAN_NAME}' no encontrado.")
#     exit()

# print(f"\n✅ Casos de prueba en el Test Plan '{TEST_PLAN_NAME}':\n")
# test_cases = get_test_cases_for_plan(plan_id)
# for case_id, versions in test_cases.items():
#     for version_id, details in versions.items():
#         external_id = details.get("external_id", "???")
#         tcase_id = details.get("tc_id", "???")
#         name = details.get("tcase_name", "Sin nombre")
#         print(f"- {external_id} :: {name}")
#         version = details.get("version", "1")
#         steps = get_test_case_steps(tcase_id, version)
#         # if steps:
#         #     for i, step in enumerate(steps, 1):
#         #         print(f"  Paso {i}:")
#         #         print(f"    Acción: {step['actions'].strip()}")
#         #         print(f"    Resultado esperado: {step['expected_results'].strip()}")
#         # else:
#         #     print("  ❗ Este caso no tiene pasos definidos.")
# attachments = tl._callServer(
#     "getAttachmentsForTestCase",
#     {"testcaseid": "40528"}
# )
# print(attachments)
ID = "7377"
API_URL = f'http://testlink.mibim.pe/testlink/lnl.php?type=exec&id={ID}&apikey={DEV_KEY}'
print(API_URL)
resp = requests.get(API_URL)
# Si crees que es HTML:
with open("respuesta_testlink.html", "w", encoding="utf-8") as f:
    f.write(resp.text)
print("✅ Archivo guardado como respuesta_testlink.html")

print(resp)