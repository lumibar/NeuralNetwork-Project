pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('') {
      steps {
        sh '''virtualenv .venv --distribute
'''
        sh '. .venv/bin/activate'
      }
    }

  }
}