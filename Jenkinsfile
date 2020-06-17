pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('install') {
      steps {
        sh 'pip install nose2'
      }
    }

  }
}