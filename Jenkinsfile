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
        stage('Git pull') {
            steps {
                git 'https://github.com/awakzdev/WorldofGames'
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