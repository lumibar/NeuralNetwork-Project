pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('Env') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh 'python -m venv .venv'
      }
    }

    stage('Deps') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh '. .venv/bin/activate && pip3 install nose2 Cython'
      }
    }

    stage('Compile') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh '. .venv/bin/activate && cd src && python setup.py build_ext --inplace'
      }
    }

    stage('Tests') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh 'mkdir reports'
        sh '. .venv/bin/activate && nose2 -c .unittest.cfg'
      }
    }

  }
  post {
    always {
      junit 'reports/*.xml'
    }

  }
}