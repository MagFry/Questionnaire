variable "heroku_api_key" {}

provider "heroku" {
  email   = "emczechowska@gmail.com"
  api_key = var.heroku_api_key
}
