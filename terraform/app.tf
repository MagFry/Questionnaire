variable "tmdb_api_key" {}

resource "heroku_app" "piis_app" {
  name   = "piis-app"
  region = "eu"

  config_vars = {
    TMDB_API_KEY = var.tmdb_api_key
    DISABLE_COLLECTSTATIC = 1
    PIIS_DEPLOYMENT = "heroku"
    # you may want to uncomment this when testing
    # PIIS_POPULATE_DB = "false"
  }

  buildpacks = [
    "heroku/python"
  ]
}

# https://www.terraform.io/docs/providers/heroku/r/addon.html
# https://elements.heroku.com/addons/heroku-postgresql
# Create a database, and configure the app to use it
resource "heroku_addon" "database" {
  app  = "${heroku_app.piis_app.name}"
  plan = "heroku-postgresql:hobby-dev"
  name = "piis-database"
}

resource "heroku_build" "piis_app" {
  app = "${heroku_app.piis_app.name}"

  source = {
    # . points to terraform/ directory
    path = "app.tar.gz"
  }
}

output "url" {
  value = "${heroku_app.piis_app.name}.herokuapp.com"
}
