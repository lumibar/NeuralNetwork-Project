pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('Venv') {
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

    stage('Deps') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh '.venv/bin/pip3 install nose2'
      }
    }

    stage('Tests') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh 'mkdir reports'
        sh '.venv/bin/python3 -m nose2 --plugin nose2.plugins.junitxml --junit-xml --junit-xml-path reports/nose2Result.xml -s src -t src *'
        junit 'reports/nose2Result.xml'
      }
    }

  }
}