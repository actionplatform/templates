output "database_url_parameter" {
  value = aws_ssm_parameter.database_url.name
}

output "endpoint" {
  value = aws_db_instance.this.address
}
