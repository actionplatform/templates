terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "random_password" "db" {
  length  = 32
  special = false
}

resource "aws_db_instance" "this" {
  identifier             = "${var.project}-${var.stage}"
  engine                 = "postgres"
  engine_version         = "16"
  instance_class         = var.instance_class
  allocated_storage      = 20
  db_name                = replace(var.project, "-", "_")
  username               = "app"
  password               = random_password.db.result
  skip_final_snapshot    = var.stage != "prod"
  deletion_protection    = var.stage == "prod"
  publicly_accessible    = false
  vpc_security_group_ids = var.security_group_ids
  db_subnet_group_name   = var.subnet_group_name

  tags = {
    Project     = var.project
    Environment = var.stage
    ManagedBy   = "terraform"
  }
}

resource "aws_ssm_parameter" "database_url" {
  name  = "/${var.project}/${var.stage}/DATABASE_URL"
  type  = "SecureString"
  value = "postgresql://app:${random_password.db.result}@${aws_db_instance.this.address}:5432/${aws_db_instance.this.db_name}"
}
