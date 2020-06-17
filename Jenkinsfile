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
      parallel {
        stage('nose2') {
          environment {
            VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
            PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
          }
          steps {
            sh 'mkdir reports'
            sh '.venv/bin/python3 -m nose2 -c .unittest.cfg'
          }
        }

        stage('pylint') {
          steps {
            echo 'Not Implemented Yet'
          }
        }

      }
    }

  }
  post {
    always {
      junit 'reports/nose2-junit.xml'
    }

  }
}