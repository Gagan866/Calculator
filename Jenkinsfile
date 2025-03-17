pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Gagan866/Calculator.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest test.py --maxfail=1 --disable-warnings
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                bat '''
                    call venv\\Scripts\\activate
                    python calculator.py
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline Succeeded!'
        }
        failure {
            echo '❌ Pipeline Failed!'
        }
    }
}
