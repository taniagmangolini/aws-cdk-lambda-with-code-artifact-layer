from aws_cdk import (
    Stack,
    aws_lambda as _lambda
)
from constructs import Construct

from codeartifact_layer import LambdaLayer


class MyProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a lambda layer
        lambda_layer = LambdaLayer(
             self,
             "LambdaLayer",
         )
    
        # create lambda function
        function = _lambda.Function(self, "lambda_function",
                                    runtime=_lambda.Runtime.PYTHON_3_9,
                                    handler="index.handler",
                                    code=_lambda.Code.from_asset("lambda"),
                                    layers=[lambda_layer.lambda_layer])