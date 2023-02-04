In GKE we can create volumes using google persistent disk

- Create a storage class
- Provision a Persistent volume using the storage class.
- Test a deployment with the persistent volume.



# Create  storage class for GKE
For example, we can classify our storage class as dev and prod. These names are arbitrary and use a name that is meaningful to you.

Prod storage class uses the pd-ssd persistent disk type for high IOPS applications (to be used with databases). While Dev storage class uses the pd-standard volume type to be used for backups and normal disk operations.


There are default storage classes available in GKE which are backed by pd-standard disks. 

Lets create a prod storage class.
## storage-class.yaml
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gold
provisioner: kubernetes.io/gce-pd
volumeBindingMode: Immediate
allowVolumeExpansion: true
reclaimPolicy: Delete
parameters:
  type: pd-standard
  fstype: ext4
  replication-type: none
```


Create the storage class.

```
kubectl apply -f storage-class.yaml
```

Type:  supports pd-standard & pd-ssd. If you don’t specify anything, it defaults pd-standard
fstype: supports ext4 and xfs. Defaults to ext4.
replication-type: This decides whether the disk is zonal or regional. If you don’t specify regional-pd, it defaults to a zonal disk.
allowVolumeExpansion: With this parameter, you can expand the persistent volume if required.
volumeBindingMode: There are two modes. Immediate and WaitForFirstConsumer. In cases where the storage is not accessible from all the nodes, use WaitForFirstConsumer so that volume binding will happen after the pod gets created.


# Create a Persistent Volume Claim

persistentVolumeClaim is the way to request storage based on a storage class and use it with a pod. The pod to Persistent volume mapping happens through PVC.

So PVC (Request) –> Storage Class (Defines Type of disk) –> Persistent Volume (Google Persistent Disk)


Create as pvc.yaml

```yaml
apiVersion: v1
 kind: PersistentVolumeClaim
 metadata:
   name: webapps-storage
 spec:
   storageClassName: gold
   accessModes:
     - ReadWriteOnce
   resources:
     requests:
       storage: 50Gi
```

Now, create the PVC.
```
kubeactl apply -f pvc.yaml
```

You can check the pv and pvc using the following commands.
```
kubectl get pv
kubectl get pvc
```

# Creating Persistent Volumes


Next step is to,

Create a Persistent volume named app-storage from the gke-pv disk
To use the persistent volume with the pod, we will create a persistent volume claim with the same name we use in the PV claimRef, ie app-storage-claim

Save the following manifest as disk-pv.yaml

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-storage
spec:
  storageClassName: "apps"
  capacity:
    storage: 50
  accessModes:
    - ReadWriteOnce
  claimRef:
    namespace: default
    name: app-storage-claim
  gcePersistentDisk:
    pdName: gke-pv
    fsType: ext4
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-storage-claim
spec:
  storageClassName: "apps"
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50
```
Create the PV & PVC.


```
kubectl apply -f disk-pv.yaml
```
You can check the pv and pvc using the following commands.

```
kubectl get pv
kubectl get pvc
```

# Example GKE Pod With Persistent Volume

pod.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-app-pod
spec:
  volumes:
    - name: app-storage
      persistentVolumeClaim:
        claimName: app-storage-claim
  containers:
    - name: nginx-app-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: app-storage
```



