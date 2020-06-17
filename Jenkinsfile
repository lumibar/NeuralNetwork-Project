pipeline {
  agent {
    docker {
      image 'python:3.8'
    }

  }
  stages {
    stage('error') {
      steps {
        sh 'python -m  venv --no-site-packages ./venv'
        sh '. ./venv/bin/activate'
      }
    }

  }
}