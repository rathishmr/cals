pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest pytest-cov'
            }
        }

        stage('Run Smoke Tests') {
            steps {
                sh 'pytest -m smoke --junitxml=reports/smoke-results.xml'
            }
        }

        stage('Run Slow Tests') {
            steps {
                sh 'pytest -m slow --junitxml=reports/slow-results.xml'
            }
        }

        stage('Run Security Tests') {
            steps {
                sh 'pytest -m security --junitxml=reports/security-results.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'reports/*.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.xml', fingerprint: true
        }
    }
}
