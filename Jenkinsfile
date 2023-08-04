pipeline {
    agent any
    stages {
        stage('Setup Python virtual env')
        {
          sh '''
          chmod +x envsetup.sh
          ./envsetup.sh
          '''
        }

        stage('Setup Gunicon')
        {
          sh '''
          chmod +x gunicorn.sh
          ./gunicorn.sh
          '''
        }    
    }
}