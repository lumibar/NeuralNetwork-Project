pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('error') {
      steps {
        sh 'python -m venv .venv'
        sh '. .venv/bin/activate && which python'
        sh 'which python'
      }
    }

  }
}