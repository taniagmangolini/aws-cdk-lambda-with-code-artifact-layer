
From MyApp run:

1. Create dist package:

 ``` 
pip install .
python3 setup.py sdist
 ``` 

2. Install twine:

 ``` 
pip install -i https://pypi.org/simple  twine
 ``` 

3. Upload to AWS CodeArtifact repo:

 ``` 
export TWINE_USERNAME=aws

export TWINE_PASSWORD=`aws codeartifact get-authorization-token --domain my-domain --domain-owner 1111111111 --query authorizationToken --output text`

export TWINE_REPOSITORY_URL=`aws codeartifact get-repository-endpoint --domain my-domain --domain-owner 1111111111 --repository my_repo --format pypi --query repositoryEndpoint --output text`

twine upload dist/*
 ``` 