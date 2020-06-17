pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }

  }
  stages {
    stage('init venv') {
      steps {
        sh '''python -c \'import sys; sys.path.append("/mnt/e/Development/Python/NeuralNetwork-Project/src")
\''''
      }
    }

  }
}