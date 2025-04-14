# SimpleTimeService on AWS ECS using Terraform

This project demonstrates how to deploy a minimal microservice container to AWS ECS Fargate using Terraform. The microservice returns the current timestamp and the IP address of the requester in JSON format.

## Project Structure

```
├── app/                   # Python Flask microservice with Dockerfile
│   ├── simple_time_service.py
│   └── Dockerfile
├── terraform/             # Terraform code to create ECS infrastructure
│   ├── main.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   ├── outputs.tf
│   └── provider.tf
```

## Requirements

- AWS Account
- AWS CLI configured (`aws configure`)
- Terraform >= 1.2
- Docker
- A DockerHub account with a public image (we use `khanpirate/simpletimeservice:latest`)

## Flask App Behavior

When you access the root (`/`) of the app, it returns:

```json
{
  "timestamp": "<UTC time>",
  "ip": "<Your IP address>"
}
```

## Setup and Deployment Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/particle41-challenge.git
cd particle41-challenge/terraform
```

### 2. Configure AWS Credentials

Use AWS CLI:

```bash
aws configure
```

Or export environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

### 3. Build and Push Docker Image

```
cd ../app
docker buildx build --platform linux/amd64 -t khanpirate/simpletimeservice:latest .
docker push khanpirate/simpletimeservice:latest
```

Ensure `terraform.tfvars` contains:

```hcl
container_image = "khanpirate/simpletimeservice:latest"
```

### 4. Deploy Infrastructure with Terraform

```bash
cd ../terraform
terraform init
terraform plan
terraform apply
```

### 5. Access the Service

After deployment, Terraform will output the ALB DNS:

```bash
alb_dns_name = simpletimeservice-alb-xxxxx.us-east-1.elb.amazonaws.com
```

Visit:  
**`http://<alb_dns_name>/`**

---

## Cleanup

To destroy the infrastructure:

```bash
terraform destroy
```

---

## Notes

- The app runs on ECS Fargate in **private subnets** using a **NAT Gateway** for outbound access.
- A Load Balancer is provisioned in **public subnets** to expose the app.
- Security groups, IAM roles, and logging are included as per AWS best practices.

---
