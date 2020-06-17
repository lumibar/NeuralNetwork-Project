pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }

  }
  stages {
    stage('Virtual Environment') {
      environment {
        VIRTUAL_ENV = '~/venv'
        PATH = 'PATH+EXTRA="$VIRTUAL_ENV/bin"'
      }
      steps {
        sh 'python3 -m venv $VIRTUAL_ENV'
        sh 'which python'
      }
    }

  }
}