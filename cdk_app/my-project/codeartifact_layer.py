from os import path
import boto3
from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_lambda_python_alpha as lambdapython
)

_dirname = path.dirname(__file__)

class LambdaLayer(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        lambda_layer_dependency_path = path.join(_dirname, "lambda_layer/build")
        domain = 'my-domain'
        domain_owner = '111111111111'
        repo_name = 'my_repo'
        region = 'us-east-1'

        code_artifact_client = boto3.client("codeartifact", region_name=region)
        code_artifact_response = code_artifact_client.get_authorization_token(
            domain=domain,
            domainOwner=domain_owner,
            durationSeconds=900
        )
        code_artifact_auth_token = code_artifact_response["authorizationToken"]

        index_url = f"https://aws:{code_artifact_auth_token}@{domain}-{domain_owner}.d.codeartifact.{region}.amazonaws.com/pypi/{repo_name}/simple/"
        
        print('#######################################################', index_url)

        self.lambda_layer = lambdapython.PythonLayerVersion(
            self,
            "MyPackage",
            entry=lambda_layer_dependency_path,
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
            bundling=lambdapython.BundlingOptions(
                environment={"PIP_INDEX_URL": index_url, "PIP_EXTRA_INDEX_URL": "https://pypi.org/simple"}
            )
        )
        
  