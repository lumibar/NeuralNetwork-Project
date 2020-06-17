pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }

  }
  stages {
    stage('Dependencies') {
      steps {
        sh 'pip3 install --no-cache-dir nose2 --user'
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