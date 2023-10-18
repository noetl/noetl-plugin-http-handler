## Install the MongoDB Community Kubernetes Operator using `kubectl`

### Build the image.
```
make build IMAGE_TAG=v0.0.1
```

### Change to the `k8s/plugin-http-handler` directory.

### Set image name/tag via kustomization.
```
kustomize edit set image localnoetl/noetl-plugin-http-handler=localnoetl/noetl-plugin-http-handler:v0.0.1
```

### Create namespace, deploy `event-store`, configure nodePort.
```
kubectl apply -k .
```
