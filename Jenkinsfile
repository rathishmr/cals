pipeline {
    agent any

    stages {

        stage('Build Freestyle Project') {
            steps {
                build job: 'python-test', propagate: false
            }
        }

        stage('Clean Pipeline Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Copy Source From python-test Workspace') {
            steps {
                bat """
                    xcopy /E /I /Y "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\python-test\\*" .
                """
            }
        }

        stage('Verify Python') {
            steps {
                bat "python --version"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Smoke Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/smoke_test.py --junitxml=smoke-results.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Smoke tests failed") }
                }
            }
        }

        stage('Run Security Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/security_test.py --junitxml=security-results.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Security tests failed") }
                }
            }
        }

        stage('Run Slow Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/slow_test.py --junitxml=slow-results.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Slow tests failed") }
                }
            }
        }

        stage('Run UI Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/test_calc_ui.py --junitxml=ui-results.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("UI tests failed") }
                }
            }
        }

        stage('Debug XML') {
            steps {
                bat "dir *.xml"
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: '*.xml'

            echo "======================================"
            echo "Final Build Status: ${currentBuild.currentResult}"
            echo "======================================"
        }
    }
}
