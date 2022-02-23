# kubernetes-based-continous-delivery

Steps
1. Clone the repo
2. Run the following commands in CMD to install all the requirements, test and run the app.
  a. Make all <br>
  b. python app.py
3. Run the following commands in CMD to create its Docker imagev to an ECR registry
  a.docker build -t container-app .
  b.docker tag container-app IMAGE_NAME
  c.docker push IMAGE_NAME
4. For AWS EKS (Requires a lot of credits) run the following commands after creating a VPC:
  a. eksctl create cluster -f create_cluster.yaml --kubeconfig=C:\Users\{user}\.kube\config
  b. aws eks --region {region} update-kubeconfig --name EKS-Demo-Cluster
  c. kubectl apply -f deployment.yaml
OR can alternatively use docker hub kubernetes service by running the following:
  a. kubectl apply -f dockerdeploy.yaml
5. For checking the deployments
  a. kubectl get deployments
  b. kubectl get pods
  c. kubectl get services
