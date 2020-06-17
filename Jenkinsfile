pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('') {
      steps {
        sh 'python -m virtualenv .venv'
        sh '. .venv/bin/activate && which python'
      }
    }

  }
}