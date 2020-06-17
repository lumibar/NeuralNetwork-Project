pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }

  }
  stages {
    stage('Virtual Environment') {
      environment {
        VIRTUAL_ENV = '"$PWD/venv"'
        PATH = 'PATH+EXTRA="$VIRTUAL_ENV/bin"'
      }
      steps {
        sh 'apt install source'
        sh 'python3 -m venv $VIRTUAL_ENV'
        sh 'which python'
        sh 'source ./venv/bin/activate'
      }
    }

    stage('Dependencies') {
      steps {
        sh 'sudo pip install nose2'
      }
    }

    stage('Test') {
      steps {
        sh 'python -m nose2 --plugin nose2.plugins.junitxml --junit-xml --junit-xml-path test_results/nose2Result.xml -s src -t src *'
        junit(testResults: 'test_results/nose2Result.xml', allowEmptyResults: true)
      }
    }

  }
}