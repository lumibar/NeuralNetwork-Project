pipeline {
  agent {
    docker {
      image 'python:3.8'
    }

  }
  stages {
    stage('install') {
      steps {
        sh 'pip install nose2'
      }
    }

  }
}