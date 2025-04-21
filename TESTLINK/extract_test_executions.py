from testlink import TestlinkAPIClient
from typing import List, Dict, Optional

# Configuración
API_URL = "http://testlink.mibim.pe/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEV_KEY = "04ded488fa8e0eddd19cb22e32092189"

PROJECT_NAME = "PDP - Nuevo Core"
TEST_PLAN_NAME = "Test Plan UAT 7: Nuevo Core"

# Conexión
tl = TestlinkAPIClient(API_URL, DEV_KEY)

# Obtener proyecto por nombre
def get_project_id_by_name(name: str) -> Optional[str]:
    projects = tl.getProjects()
    for p in projects:
        if p["name"] == name:
            return p["id"]
    return None

# Obtener test plan por nombre
def get_test_plan_id_by_name(project_id: str, plan_name: str) -> Optional[str]:
    test_plans = tl.getProjectTestPlans(project_id)
    for plan in test_plans:
        if plan["name"] == plan_name:
            return plan["id"]
    return None

# Obtener casos de prueba del plan
def get_test_cases_for_plan(plan_id: str) -> Dict:
    return tl.getTestCasesForTestPlan(plan_id)

# Ejecutar flujo
project_id = get_project_id_by_name(PROJECT_NAME)
if not project_id:
    print(f"❌ Proyecto '{PROJECT_NAME}' no encontrado.")
    exit()

plan_id = get_test_plan_id_by_name(project_id, TEST_PLAN_NAME)
if not plan_id:
    print(f"❌ Test Plan '{TEST_PLAN_NAME}' no encontrado.")
    exit()

print(f"\n✅ Casos de prueba en el Test Plan '{TEST_PLAN_NAME}':\n")
test_cases = get_test_cases_for_plan(plan_id)

for case_id, versions in test_cases.items():
    for version_id, details in versions.items():
        external_id = details.get("external_id", "???")
        name = details.get("tcase_name", "Sin nombre")
        print(f"- {external_id} :: {name}")
