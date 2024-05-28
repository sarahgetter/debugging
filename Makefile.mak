# Variables
IMAGE_NAME = python-app
PROJECT_ID = your-gcp-project-id
CLUSTER_NAME = your-cluster-name
ZONE = your-cluster-zone

# Commands
build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 4000:80 $(IMAGE_NAME)

push:
	docker tag $(IMAGE_NAME) gcr.io/$(PROJECT_ID)/$(IMAGE_NAME)
	docker push gcr.io/$(PROJECT_ID)/$(IMAGE_NAME)

deploy:
	kubectl apply -f kubernetes-deployment.yaml

# GCP specific commands
gcp-auth:
	gcloud auth configure-docker

gcp-cluster:
	gcloud container clusters get-credentials $(CLUSTER_NAME) --zone $(ZONE)

clean:
	docker rmi $(IMAGE_NAME)
