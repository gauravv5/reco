from aana.sdk import AanaSDK

from reco.configs.deployments import deployments
from reco.configs.endpoints import endpoints

aana_app = AanaSDK(name="reco")

for deployment in deployments:
    aana_app.register_deployment(**deployment)

for endpoint in endpoints:
    aana_app.register_endpoint(**endpoint)

if __name__ == "__main__":
    aana_app.connect()
    aana_app.migrate()
    aana_app.deploy()
