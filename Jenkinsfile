pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Run Score flask') {
            steps {
                sh 'python ./MainScores.py'
            }
        }
        stage('Test with E2E') {
            steps {
                sh 'python ./e2e.py'
            }
        }
    }
}