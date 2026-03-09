pipeline {
    agent any

    stages {

        stage('Prepare Workspace') {
            steps {
                build job: 'python-test', propagate: false
                deleteDir()

                bat """
                xcopy /E /I /Y "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\python-test\\*" .
                """
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

        // ---------------- BUILD 1 ----------------

        stage('Build 1 - Simple Calculator Tests') {
            environment {
                CALC_MODULE = "calc"
            }

            parallel {

                stage('Smoke Tests') {
                    steps {
                        bat "python -m pytest tests/smoke_test.py --junitxml=b1-smoke.xml"
                    }
                }

                stage('Security Tests') {
                    steps {
                        bat "python -m pytest tests/security_test.py --junitxml=b1-security.xml"
                    }
                }

            }
        }

        

        // ---------------- UPGRADE ----------------

        stage('Upgrade to Scientific Version') {
            steps {
                echo "Switching to ScientificCalculator for Build 2"
            }
        }

        // ---------------- BUILD 2 ----------------

        stage('Build 2 - Scientific Calculator Tests') {
            environment {
                CALC_MODULE = "calc2"
            }

            parallel {

                stage('Sanity Tests') {
                    steps {
                        bat "python -m pytest tests/sanity_test.py --junitxml=b2-sanity.xml"
                    }
                }

                stage('Slow Tests') {
                    steps {
                        bat "python -m pytest tests/slow_test.py --junitxml=b2-slow.xml"
                    }
                }

                stage('UI Tests') {
                    steps {
                        bat "python -m pytest tests/test_calc_ui.py --junitxml=b2-ui.xml"
                    }
                }

            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: "*.xml"
        }
    }
}
