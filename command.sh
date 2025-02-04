helm upgrade --install canary ./canary --namespace business-service \
--set defaults.host=business-service.business-service.svc.cluster.local \
--set defaults.namespace=business-service 

helm upgrade --install business-service ./business-service --namespace business-service \
--set stable.image.tag=v5

helm upgrade --install business-service ./business-service --namespace business-service \
--set canary.image.tag=v6
--set canary.replicaCount=1

helm template  --install business-service ./business-service --namespace business-service \
--set stable.image.tag=v5