# Declarative way of using Kubectl to interact with Kubernenets

Generate the yaml format from existing deployments/pods
```
kubectl get deployment <deployment-name> -o yaml
kubectl get pod <pod-name> -o yaml
kubectl get service <service-name> -o yaml
```

## Create a Pod:
Create a file called pod.yaml and fill the below info.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

Deploy the pod
```
 kubectl apply -f pod.yaml
```


## Create a nginx deployment
Create a file called deployment.yaml and fill the below info.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-deployment
spec:
 replicas: 2
 selector:
   matchLabels:
     app: nginx
 template:
   metadata:
     labels:
       app: nginx
   spec:
     containers:
     - name: nginx
       image: nginx:1.14.2
       ports:
       - containerPort: 80
```


Apply the deployment:
```
 kubectl apply -f deployment.yaml
```

## Create a service
Create a file called service.yaml and add the content.
```yaml
apiVersion: v1
kind: Service
metadata:
 name: nginx
 labels:
run: nginx
spec:
 ports:
 - port: 80
   protocol: TCP
 selector:
run: nginx
```


Apply the service creation:
```
 kubectl apply -f service.yaml
```

Delete a deployment:
```
 kubectl apply -f deployment.yaml
```
