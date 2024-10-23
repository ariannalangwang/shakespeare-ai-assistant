# FAST API
```
pip install "fastapi[all]"

uvicorn main:app --reload
```


# Test with Postman
URL - http://127.0.0.1:80/response
(POST)

```json
{
  "text": "Who is the hero of the story?"
}
```


# Docker Commands
```
docker build -t <image-name> .
 
docker run --rm --name <container_name> -e OPENAI_API_KEY=your_openai_api_key -e ASSISTANT_ID=your_assistant_id -p 80:80 <image-name>

docker tag <image-name> <docker-username>/<image-name>

docker push <docker-username>/<image-name>
```


# Important Code for Docker
For Mac users:
```
docker buildx build --platform=linux/amd64 -t <docker-username>/<image-name>:<tag> .
docker push <docker-username>/<image-name>:<tag>
```


# Kubernetes Commands
```
kubectl create secret generic ai-assistant-secret \
  --from-literal=OPENAI_API_KEY=<openai-api-key> \
  --from-literal=ASSISTANT_ID==<assistant-id>

kubectl get secrets
kubectl describe secret ai-assistant-secret

kubectl apply -f deploy

kubectl delete -f deploy
kubectl delete secret ai-assistant-secret

kubectl get pods,svc,deployments,secrets
```


# GCP Commands
```
gcloud auth login

gcloud config set project <YOUR_PROJECT_ID>
gcloud config set project aw-mlops-project


gcloud container clusters create my-cluster --num-nodes=2 --zone=us-west1-a

gcloud container clusters get-credentials my-cluster --zone=us-west1-a

kubectl get nodes

kubectl get svc 
## We can use the service's EXTERNAL-IP to access the app!


gcloud container clusters delete my-cluster --zone=us-west1-a
```