# minikube_test

## installation on macos

```
brew install minikube
```

```
minikube version
```

```
minikube start --driver=docker
```

```
kubectl get nodes
```

## full reset

```
minikube delete
minikube start --driver=docker
```

## switch docker context to minikube

```
eval $(minikube -p minikube docker-env)
```

## get all

```
kubectl get all
```

## build an image for minikube

```
docker build \
  -t demo-api:latest .
```

## apply deployment and service, configmap, secret

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
```

## service access

```
minikube service demo-api
```

## watch for endpoint

```
watch -n 0.1 curl http://127.0.0.1:51889/
```


## increase numbers of replicas 

```
kubectl scale deployment demo-api --replicas=3
kubectl get pods
```

## rolling update 

```
kubectl rollout restart deployment/demo-api
```

## switch docker context back to local from minikube

```
eval $(minikube docker-env -u)
```

## namespaces

### create

```
kubectl create namespace dev
```

### list 

```
kubectl get namespaces
```

### make default 

```
kubectl config set-context --current --namespace=dev
```

### get all in all namespaces

```
kubectl get all -A
```

### apply everything inside the overlays/prod

```
kubectl apply -k overlays/prod
```

### get pods for dev namespace

```
kubectl get pods -n dev
```

## stop minikube (not delete!)

```
minikube stop
```

