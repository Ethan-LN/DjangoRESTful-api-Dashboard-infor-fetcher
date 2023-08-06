pipeline {
    agent any
    stages {
        stage('Setup Python virtual env') {
            steps {
                sh '''
                chmod +x envsetup.sh
                ./envsetup.sh
                '''
                }

        stage('Setup Gunicon') {
            steps {
                sh '''
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
                }
        }
        }
    }
