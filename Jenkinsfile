pipeline {
    agent any

    stages {

        stage('Install') {
            steps {
                sh 'pip install pytest pytest-cov coverage'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --cov=. --cov-report=html --cov-report=term --cov-fail-under=80'
            }
        }

        stage('Archive Coverage') {
            steps {
                archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
            }
        }
    }
}
