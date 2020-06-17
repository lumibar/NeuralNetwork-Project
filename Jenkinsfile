pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('1') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh 'python -m venv .venv'
        sh '. .venv/bin/activate && which python'
        sh 'which python'
      }
    }

    stage('2') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh '.venv/bin/pip3 install nose2'
      }
    }

  }
}