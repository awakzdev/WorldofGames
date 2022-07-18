pipeline {
    agent {
        dockerfile true
    }
        stage('run') {
            steps {
                sh 'python ./MainScores.py &'
            }
        }
        stage('test') {
            steps {
                sh 'python ./e2e.py'
            }
        }
        stage('build') {
            steps {
                sh 'docker build -t awakz/worldofgames:latest .'
            }
        }
        stage('pre-push (login)') {
            steps {
                sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'
            }
        }
        stage('push') {
            steps {
                sh 'docker push awakz/worldofgames:latest'
            }
        }
    }
}
