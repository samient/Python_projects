Kubectl cluster-info
Basic Commands

Command	Description
kubectl get pods	#List all pods in the current namespace
kubectl get nodes	#List all nodes in the cluster
kubectl get services	#List all services
kubectl get deployments	#List all deployments
kubectl get rs or kubectl get replicasets	#List ReplicaSets
kubectl get all	#List all objects in the namespace
kubectl describe pod <pod-name>	#Detailed info of a specific pod
kubectl describe node <node-name>	#Detailed info of a node
kubectl get events	#Show cluster events
kubectl get namespaces	#List all namespaces
Creating and Applying Resources
Command	Description
kubectl apply -f <file>.yaml	         # Apply a config file
kubectl create -f <file>.yaml	         # Create resource(s) from file
kubectl create deployment <name> --image=<image>	         # Create a deployment quickly
kubectl expose deployment <name> --port=<port> --type=NodePort	         # Create service for a deployment
Managing Pods and Containers
Command	Description
kubectl logs <pod-name>	         # View logs from a pod
kubectl exec -it <pod-name> -- bash	         # Access shell in a running pod
kubectl port-forward <pod-name> <local-port>:<container-port>	         # Port forward for access
kubectl delete pod <pod-name>	         # Delete a specific pod

Scaling & Updating
Command	Description
kubectl scale deployment <name> --replicas=<num>	         # Scale a deployment
kubectl rollout status deployment/<name>	         # Check rollout status
kubectl rollout undo deployment/<name>	#Undo a deployment
kubectl edit deployment <name>	#Edit deployment live in editor

Delete Resources
Command	Description
kubectl delete -f <file>.yaml	#Delete resources defined in file
kubectl delete pod <name>	#Delete a specific pod
kubectl delete service <name>	#Delete a service
kubectl delete deployment <name>	#Delete a deployment
________________________________________
Namespace & Context
Command	Description
kubectl config get-contexts	#View available contexts
kubectl config use-context <name>	#Switch context
kubectl config current-context	Show #current context
kubectl get pods --all-namespaces	#List pods in all namespaces
kubectl config set-context --current --namespace=<ns>	#Set default namespace
________________________________________
Advanced & Debug
Command	Description
kubectl top pod	Show #CPU/Memory usage of pods (metrics-server needed)
kubectl top node	#S#how resource usage per node
kubectl get componentstatus	Show health of cluster components
kubectl cp <pod-name>:/path/in/pod /local/path	#Copy file from pod
kubectl auth can-i <action> <resource>	#Check RBAC permissions
kubectl explain <resource>	#Explain resource (like man page)
kubectl api-resources	#List all API resources
kubectl api-versions	#List all API versions#
