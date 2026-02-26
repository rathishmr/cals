pipeline {
    agent any

    environment {
        APP_PORT = "8080"
    }

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Directories') {
            steps {
                bat '''
                if not exist reports mkdir reports
                if not exist dashboard mkdir dashboard
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                pip install pytest pytest-cov selenium webdriver-manager flask
                '''
            }
        }

        stage('Start Calculator App') {
            steps {
                bat '''
                echo Starting Calculator App...
                start /B python app.py
                timeout /t 5
                '''
            }
        }

        stage('Run Tests') {
            parallel {

                stage('Smoke Tests') {
                    steps {
                        bat '''
                        pytest -m smoke ^
                        --junitxml=reports/smoke.xml ^
                        --cov=. ^
                        --cov-report=xml:reports/coverage.xml ^
                        --cov-report=term ^
                        --cov-fail-under=80
                        '''
                    }
                }

                stage('Slow Tests') {
                    steps {
                        bat '''
                        pytest -m slow ^
                        --junitxml=reports/slow.xml
                        '''
                    }
                }

                stage('Security Tests') {
                    steps {
                        bat '''
                        pytest -m security ^
                        --junitxml=reports/security.xml
                        '''
                    }
                }

                stage('UI Tests') {
                    steps {
                        bat '''
                        pytest tests/test_calculator_ui.py ^
                        --junitxml=reports/ui.xml
                        '''
                    }
                }
            }
        }

        stage('Publish JUnit Reports') {
            steps {
                junit 'reports/*.xml'
            }
        }

        stage('Generate Dashboard') {
            steps {
                bat '''
                if not exist dashboard mkdir dashboard
                python dashboard.py
                dir dashboard
                '''
            }
        }

        stage('Verify Dashboard Exists') {
            steps {
                script {
                    if (!fileExists('dashboard/summary.html')) {
                        error("Dashboard summary.html NOT found!")
                    }
                }
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'dashboard',
                    reportFiles: 'summary.html',
                    reportName: 'Calculator Test Dashboard'
                ])
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
                archiveArtifacts artifacts: 'dashboard/**', fingerprint: true
            }
        }
    }

    post {

        always {
            echo "Build Completed"
        }

        success {
            echo "Build SUCCESSFUL 🎉"
        }

        failure {
            echo "Build FAILED ❌"
        }

        cleanup {
            bat '''
            echo Stopping Python processes...
            taskkill /F /IM python.exe 2>NUL
            '''
        }
    }
}
