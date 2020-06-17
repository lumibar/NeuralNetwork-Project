pipeline {
  agent {
    docker {
      image 'python:3.8'
    }

  }
  stages {
    stage('venv') {
      steps {
        sh 'python -m  venv ./venv'
        sh '. ./venv/bin/activate'
        sh 'which python'
      }
    }

    stage('install') {
      steps {
        sh 'pip install --no-cache-dir --user nose2'
      }
    }

  }
}