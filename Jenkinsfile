pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('error') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}'
      }
      steps {
        sh 'python -m venv .venv'
        sh '. .venv/bin/activate && which python'
        sh 'which python'
      }
    }

  }
}