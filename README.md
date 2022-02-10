# kubernetes-based-continous-delivery

Steps
1. Clone the repo
2. Run the following commands in CMD to install all the requirements, test and run the app.
  a. Make all 
  b.python app.py
3. Run the following commands in CMD to create its Docker imagev to an ECR registry
  a.docker build -t container-app .
  b.docker tag container-app $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
  c.docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
