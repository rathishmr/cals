pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest pytest-cov coverage'
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                sh 'pytest --cov=. --cov-report=html --cov-report=term --cov-fail-under=80'
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }
}
