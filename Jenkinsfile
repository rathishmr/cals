pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_TYPE',
            choices: ['all','build1','build2','smoke','security','slow','ui','sanity'],
            description: 'Select build or specific test type to run'
        )
    }

    stages {

        stage('Prepare Workspace') {
            steps {
                deleteDir()
                git url: 'https://github.com/rathishmr/cals.git', branch: 'main'
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
            when {
                expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build1' || params.TEST_TYPE == 'smoke' || params.TEST_TYPE == 'security' || params.TEST_TYPE == 'slow' || params.TEST_TYPE == 'ui' }
            }

            environment {
                CALC_MODULE = "calc"
            }

            parallel {

                stage('Smoke Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build1' || params.TEST_TYPE == 'smoke' } }
                    steps {
                        bat "python -m pytest tests/smoke_test.py --junitxml=b1-smoke.xml"
                    }
                }

                stage('Security Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build1' || params.TEST_TYPE == 'security' } }
                    steps {
                        bat "python -m pytest tests/security_test.py --junitxml=b1-security.xml"
                    }
                }

                stage('Slow Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build1' || params.TEST_TYPE == 'slow' } }
                    steps {
                        bat "python -m pytest tests/slow_test.py --junitxml=b1-slow.xml"
                    }
                }

                stage('UI Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build1' || params.TEST_TYPE == 'ui' } }
                    steps {
                        bat "python -m pytest tests/test_calc_ui.py --junitxml=b1-ui.xml"
                    }
                }
            }
        }

        // ---------------- UPGRADE ----------------

        stage('Upgrade to Scientific Version') {
            when {
                expression { params.TEST_TYPE != 'build1' }
            }
            steps {
                echo "Switching to ScientificCalculator for Build 2"
            }
        }

        // ---------------- BUILD 2 ----------------

        stage('Build 2 - Scientific Calculator Tests') {
            when {
                expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build2' || params.TEST_TYPE == 'smoke' || params.TEST_TYPE == 'security' || params.TEST_TYPE == 'slow' || params.TEST_TYPE == 'ui' || params.TEST_TYPE == 'sanity' }
            }

            environment {
                CALC_MODULE = "calc2"
            }

            parallel {

                stage('Sanity Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build2' || params.TEST_TYPE == 'sanity' } }
                    steps {
                        bat "python -m pytest tests/sanity_test.py --junitxml=b2-sanity.xml"
                    }
                }

                stage('Smoke Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build2' || params.TEST_TYPE == 'smoke' } }
                    steps {
                        bat "python -m pytest tests/smoke_test.py --junitxml=b2-smoke.xml"
                    }
                }

                stage('Security Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build2' || params.TEST_TYPE == 'security' } }
                    steps {
                        bat "python -m pytest tests/security_test.py --junitxml=b2-security.xml"
                    }
                }

                stage('Slow Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build2' || params.TEST_TYPE == 'slow' } }
                    steps {
                        bat "python -m pytest tests/slow_test.py --junitxml=b2-slow.xml"
                    }
                }

                stage('UI Tests') {
                    when { expression { params.TEST_TYPE == 'all' || params.TEST_TYPE == 'build2' || params.TEST_TYPE == 'ui' } }
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

            echo "======================================"
            echo "Selected Mode: ${params.TEST_TYPE}"
            echo "Pipeline Completed"
            echo "======================================"
        }
    }
}
