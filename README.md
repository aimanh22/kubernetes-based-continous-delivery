# kubernetes-based-continous-delivery

Steps
1. Clone the repo
2. Run the following commands in CMD to install all the requirements, test and run the app. <br>
  a. Make all <br>
  b. python app.py <br>
3. Run the following commands in CMD to create its Docker imagev to an ECR registry <br>
  a.docker build -t container-app . <br>
  b.docker tag container-app IMAGE_NAME <br>
  c.docker push IMAGE_NAME <br>
4. For AWS EKS (Requires a lot of credits) run the following commands after creating a VPC: <br>
  a. eksctl create cluster -f create_cluster.yaml --kubeconfig=C:\Users\{user}\.kube\config <br>
  b. aws eks --region {region} update-kubeconfig --name EKS-Demo-Cluster <br>
  c. kubectl apply -f deployment.yaml <br>
OR can alternatively use docker hub kubernetes service by running the following: <br>
  a. kubectl apply -f dockerdeploy.yaml <br>
5. For checking the deployments <br>
  a. kubectl get deployments <br>
  b. kubectl get pods <br>
  c. kubectl get services <br>
