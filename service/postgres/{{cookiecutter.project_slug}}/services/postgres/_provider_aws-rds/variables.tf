variable "project" {
  type    = string
  default = "{{ cookiecutter.project_slug }}"
}

variable "stage" {
  type    = string
  default = "dev"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "instance_class" {
  type    = string
  default = "db.t4g.micro"
}

variable "security_group_ids" {
  type = list(string)
}

variable "subnet_group_name" {
  type = string
}
