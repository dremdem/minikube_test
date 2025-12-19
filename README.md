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
  --build-arg APP_VERSION=1.0 \
  -t demo-api:latest .
```


## apply deployment and service

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## service access

```
minikube service demo-api
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