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

## build an image for minikube

```
docker build \
  -t demo-api:latest .
```

§
## apply deployment and service, configmap

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml
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

## stop minikube (not delete!)

```
minikube stop
```

