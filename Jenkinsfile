pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        script{
       echo "Git checkout"
       git branch: 'main', url: 'https://github.com/parrot-07/Three-tier-Flask-app.git'
    }
}
}

    stage('Build Docker images') {
      steps {
        script{
         echo "Building backend image"
        sh  "docker compose build"
        }
      }
    }

    stage('Deploy') {
      steps {
        script{
          echo "stopping old containers"
          sh "docker compose down"
          echo "Starting new containers"
          sh "docker compose up -d"
          
          }
        }
      }
  }
}
