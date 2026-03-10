pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_SMOKE', defaultValue: true, description: 'Run Smoke Tests')
        booleanParam(name: 'RUN_SECURITY', defaultValue: true, description: 'Run Security Tests')
        booleanParam(name: 'RUN_SLOW', defaultValue: true, description: 'Run Slow Tests')
        booleanParam(name: 'RUN_UI', defaultValue: true, description: 'Run UI Tests')
        booleanParam(name: 'RUN_SANITY', defaultValue: true, description: 'Run Sanity Tests (Build2)')
    }

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
                    when { expression { params.RUN_SMOKE } }
                    steps {
                        bat "python -m pytest tests/smoke_test.py --junitxml=b1-smoke.xml"
                    }
                }

                stage('Security Tests') {
                    when { expression { params.RUN_SECURITY } }
                    steps {
                        bat "python -m pytest tests/security_test.py --junitxml=b1-security.xml"
                    }
                }

                stage('Slow Tests') {
                    when { expression { params.RUN_SLOW } }
                    steps {
                        bat "python -m pytest tests/slow_test.py --junitxml=b1-slow.xml"
                    }
                }

                stage('UI Tests') {
                    when { expression { params.RUN_UI } }
                    steps {
                        bat "python -m pytest tests/test_calc_ui.py --junitxml=b1-ui.xml"
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
                    when { expression { params.RUN_SANITY } }
                    steps {
                        bat "python -m pytest tests/sanity_test.py --junitxml=b2-sanity.xml"
                    }
                }

                stage('Smoke Tests') {
                    when { expression { params.RUN_SMOKE } }
                    steps {
                        bat "python -m pytest tests/smoke_test.py --junitxml=b2-smoke.xml"
                    }
                }

                stage('Security Tests') {
                    when { expression { params.RUN_SECURITY } }
                    steps {
                        bat "python -m pytest tests/security_test.py --junitxml=b2-security.xml"
                    }
                }

                stage('Slow Tests') {
                    when { expression { params.RUN_SLOW } }
                    steps {
                        bat "python -m pytest tests/slow_test.py --junitxml=b2-slow.xml"
                    }
                }

                stage('UI Tests') {
                    when { expression { params.RUN_UI } }
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
