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
                sh 'pytest --cov=. --cov-report=xml --cov-report=term --cov-fail-under=80'
            }
        }

        stage('Coverage Report') {
            steps {
                recordCoverage tools: [[parser: 'COBERTURA', pattern: 'coverage.xml']]
            }
        }
    }
}
