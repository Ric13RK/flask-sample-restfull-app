// Output variables

output "ecr_repo_name" {
  value = aws_ecr_repository.rishi_test_flask_app.repository_url
}