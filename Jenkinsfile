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

  }
}