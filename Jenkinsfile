pipeline {
    agent any

    stages {
        stage('Run unit tests') {
            steps {
                withPythonEnv('python3.12') {
                    sh 'pip install -r requirements.txt'
                    sh 'python -m pytest'
                }
            }
        }
        stage('Build docker image') {
            steps {
                sh 'docker build -t localhost:5000/example-flask-api .'
            }
        }
        stage("Push docker image to registry") {
            steps {
                sh "docker push localhost:5000/example-flask-api"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}