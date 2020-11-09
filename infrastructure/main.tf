// Main Config

terraform {
  # https://github.com/runatlantis/atlantis/issues/1153
  # # # store state in remote location
  # # # in this case its aws s3 (also use enable bucket versioning)
  # # backend "s3" {
  # #   bucket         = ""
  # #   key            = "terraform.tfstate"
  # #   region         = ""
  # #   dynamodb_table = ""
  # # }
  # required_version = ">= 0.12"

  # # install only plugin version (best practice)
  # required_providers {
  #   aws = {
  #     source = "hashicorp/aws"
  #     version = "~> 3.14"
  #   }
  # }
}