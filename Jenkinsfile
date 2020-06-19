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
        sh '.venv/bin/pip3 install nose2 Cython'
      }
    }

    stage('Compile') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh 'find ./src -name "*.pxd" | xargs -I X bash -c \'x=X;.venv/bin/python3 -m cythonize -3 -i ${x:0:-2}y\''
      }
    }

    stage('Tests') {
      environment {
        VIRTUAL_ENV = '/var/jenkins_home/workspace/NeuralNetwork-Project_master/.venv'
        PATH = '"${VIRTUAL_ENV}/bin:${PATH}"'
      }
      steps {
        sh 'mkdir reports'
        sh '.venv/bin/python3 -m nose2 -c .unittest.cfg'
      }
    }

  }
  post {
    always {
      junit 'reports/*.xml'
    }

  }
}