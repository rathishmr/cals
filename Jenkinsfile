pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    ${PYTHON} -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests in Parallel') {
            parallel {

                stage('Smoke Tests') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            pytest -m smoke -n auto \
                            --cov=calculator \
                            --cov-report=xml \
                            --cov-report=html \
                            --junitxml=reports/smoke.xml
                        '''
                    }
                }

                stage('Security Tests') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            pytest -m security -n auto \
                            --junitxml=reports/security.xml
                        '''
                    }
                }

                stage('Slow Tests') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            pytest -m slow -n auto \
                            --junitxml=reports/slow.xml
                        '''
                    }
                }
            }
        }

        stage('Coverage Check') {
            steps {
                sh '''
                    . venv/bin/activate
                    coverage xml
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'

            publishHTML(target: [
                reportDir: 'htmlcov',
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])
        }

        success {
            script {
                def coverage = sh(
                    script: ". venv/bin/activate && coverage report | grep TOTAL | awk '{print \$4}' | sed 's/%//'",
                    returnStdout: true
                ).trim()

                if (coverage.toInteger() < 80) {
                    error "Build failed: Coverage below 80% (Current: ${coverage}%)"
                }
            }
        }
    }
}
