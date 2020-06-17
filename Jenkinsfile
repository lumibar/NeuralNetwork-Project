pipeline {
  agent {
    docker {
      image 'python:3.8'
    }

  }
  stages {
    stage('') {
      steps {
        sh 'python -m --no-site-packages venv ./venv'
        sh '. ./venv/bin/activate'
      }
    }

  }
}