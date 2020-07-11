## Script to deploy project

function get-deployed{
    $env:FLASK_APP=".\src\flask_app.py"
    flask run
}

get-deployed