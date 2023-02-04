## Commands:

```
gcloud config set project <project-name>
gcloud config set compute/zone us-central1-a
```

## Create a cluster
```
gcloud container clusters create edureka-gke-cluster --num-nodes=1 --zone us-central1-a --project <project-name>
```

## Get credentials
```
gcloud container clusters get-credentials edureka-gke-cluster
```

To interact with the cluster, we need to use kubectl tool

## Check the version:
```
kubectl version 
```

## Get number of nodes
```
kubectl get nodes
```

## Check cluster info:
```
kubectl cluster-info
```

## Deploy a container
```
kubectl run webserver --image=gcr.io/project-dev-demo/edureka-webserver:v1
```


## Describe a pod
```
kubectl describe pod webserver
```

## Get pods
```
kubectl get pods
```

## Delete a pod
```
kubectl delete pod webserver
```


## Create a deployment
```
kubectl create deployment webserver-deployment --image=gcr.io/project-dev-demo/edureka-webserver-2:v1
```

## Get the deployment
```
kubectl get deployments
```

## Show the replicates:
```
kubectl get replicaset
```

## Show the pods
```
kubectl get pods
```


## Show the default k8s service
```
kubectl get services
```

## Expose deployment via Load Balancer
```
kubectl expose deployment webserver-deployment  --port 80 --type LoadBalancer
```

## Get services
```
kubectl get services
```

# Scaling

## Scale deployment - number of pods
```
kubectl scale deployment webserver-deployment  --replicas 3
```
## verify the pods
```
kubectl get pods
```

## Get services
```
kubectl get services
```


## Delete a pod
```
kubectl delete pod < name>
```

# 4 way autoscaling

## Get the current node-pool
```
gcloud container node-pools list --cluster edureka-gke-cluster
```

## Resize the node pool - add more nodes
```
gcloud container clusters resize edureka-gke-cluster  --node-pool default-pool --num-nodes 2
```

## View the pods 
```
Kubectl get pods
```


## Resize the pods - resize to 5 pods
```
kubectl scale deployment webserver-deployment  --replicas 5
```