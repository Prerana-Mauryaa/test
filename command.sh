helm upgrade --install --namespace business-service \
--set defaults.host=business-service.business-service.svc.cluster.local \
--set defaults.namespace=business-service canary ./canary


helm upgrade --install --namespace business-service \
--values ./business-service/stable-values.yaml \
--set image.tag=v1 business-service ./business-service

helm upgrade --install --namespace business-service \
--values ./business-service/canary-values.yaml \
--set image.tag=v2 business-service ./business-service
