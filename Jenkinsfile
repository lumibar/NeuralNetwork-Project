pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }

  }
  stages {
    stage('Virtual Environment') {
      steps {
        sh 'python3 -m venv ./venv'
        sh 'source ./venv/bin/activate'
        sh 'which python'
      }
    }

  }
}