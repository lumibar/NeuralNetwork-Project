pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }

  }
  stages {
    stage('Virtual Environment') {
      environment {
        VIRTUAL_ENV = '/opt/venv'
        PATH = '"$VIRTUAL_ENV/bin:$PATH"'
      }
      steps {
        sh 'python3 -m venv $VIRTUAL_ENV'
        sh 'which python'
      }
    }

  }
}