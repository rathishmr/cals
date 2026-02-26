pipeline {
    agent any

    environment {
        APP_PORT = "5000"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python -m pip install --upgrade pip
                pip install pytest pytest-cov junitparser selenium webdriver-manager flask
                mkdir -p reports
                mkdir -p dashboard
                '''
            }
        }

        stage('Start Calculator Application') {
            steps {
                sh '''
                echo "Starting Calculator App..."
                nohup python app.py > app.log 2>&1 &
                sleep 5
                '''
            }
        }

        stage('Run Tests in Parallel') {
            parallel {

                stage('Smoke Tests') {
                    steps {
                        sh '''
                        pytest -m smoke \
                        --junitxml=reports/smoke.xml \
                        --cov=. \
                        --cov-report=xml:reports/coverage.xml \
                        --cov-report=term \
                        --cov-fail-under=80
                        '''
                    }
                }

                stage('Slow Tests') {
                    steps {
                        sh '''
                        pytest -m slow \
                        --junitxml=reports/slow.xml
                        '''
                    }
                }

                stage('Security Tests') {
                    steps {
                        sh '''
                        pytest -m security \
                        --junitxml=reports/security.xml
                        '''
                    }
                }

                stage('UI Tests') {
                    steps {
                        sh '''
                        pytest tests/test_calc_ui.py \
                        --junitxml=reports/ui.xml
                        '''
                    }
                }
            }
        }

        stage('Publish JUnit Results') {
            steps {
                junit 'reports/*.xml'
            }
        }

        stage('Generate HTML Dashboard') {
            steps {
                sh '''
                python dashboard.py
                '''
            }
        }

        stage('UI Verification Stage') {
            steps {
                script {
                    echo "Verifying generated files..."

                    if (!fileExists('reports/smoke.xml')) {
                        error("Smoke report missing!")
                    }

                    if (!fileExists('reports/ui.xml')) {
                        error("UI test report missing!")
                    }

                    if (!fileExists('dashboard/summary.html')) {
                        error("Dashboard not generated!")
                    }

                    echo "All reports verified successfully ✅"
                }
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'dashboard/**', fingerprint: true
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
    }

    post {

        always {
            echo "Build Finished"
        }

        success {
            echo "Build SUCCESSFUL 🎉"
        }

        failure {
            echo "Build FAILED ❌"
        }

        cleanup {
            sh '''
            echo "Stopping Calculator App..."
            pkill -f app.py || true
            '''
        }
    }
}
