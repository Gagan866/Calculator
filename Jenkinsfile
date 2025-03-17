pipeline {
    agent any  // Run on any available Jenkins agent

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Gagan866/Calculator.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                bat 'python -m venv venv'  // Create a virtual environment
                bat 'venv\\Scripts\\activate'  // Activate virtual environment (Windows)
                bat 'pip install -r requirements.txt'  // Install dependencies
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest test_calculator.py'  // Run tests
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed!'
        }
    }
}
