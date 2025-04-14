variable "region" {
    default = "us-east-1"
}

variable "app_name" {
    default = "simple-time-service"
}

variable "container_image" {
    description = "Docker image for ECS task"
    type = strings
}