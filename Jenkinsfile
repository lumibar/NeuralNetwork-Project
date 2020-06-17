pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }

  }
  stages {
    stage('init') {
      steps {
        sh '''python -c \'import sys; sys.path.append("./src")
\''''
        sh 'ls -la'
      }
    }

    stage('Unit  Tests') {
      steps {
        sh 'python -m nose2 --plugin nose2.plugins.junitxml --junit-xml --junit-xml-path test_results/nose2Result.xml -s src -t src *'
        junit './test_results/nose2Result.xml'
      }
    }

  }
}