terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 5.92"
        }
    }
}

provider "aws" {
   region = "us-east-1"
}

resource "aws_s3_bucket" "resume_bucket" {
  bucket = "aminetraibi.com"
}

resource "aws_dynamodb_table" "visitor_count" {
  name = "visitor_count"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"
    attribute {
        name = "id"
        type = "S"
    }
}

resource "aws_lambda_function" "update_visitor_count" {
    function_name = "update_visitor_count"
    runtime = "python3.9"
    handler = "lambda_function.lambda_handler"
    role = "arn:aws:iam::518216637569:role/service-role/update_visitor_count-role-bh9qkv93"
    filename = "lambda_function.zip"
  
}
resource "aws_iam_role" "lambda_exec" {
  name = "update_visitor_count-role-bh9qkv93"
  path = "/service-role/"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "dynamodb_access" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
}