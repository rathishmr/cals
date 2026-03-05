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

        // =====================================
        // BUILD 1 : SIMPLE CALCULATOR
        // =====================================

        stage('Build 1 - Simple Calculator') {
            steps {
                echo "Running tests on Simple Calculator (calc.py)"
            }
        }

        stage('Build 1 - Smoke Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/smoke_test.py --junitxml=b1-smoke.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Build1 Smoke tests failed") }
                }
            }
        }

        stage('Build 1 - Security Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/security_test.py --junitxml=b1-security.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Build1 Security tests failed") }
                }
            }
        }

        // =====================================
        // BACKUP ORIGINAL CALCULATOR
        // =====================================

        stage('Backup Original Calculator') {
            steps {
                echo "Backing up calc.py before upgrade"
                bat "copy /Y calc.py calc_backup.py"
            }
        }

        // =====================================
        // BUILD 2 : SCIENTIFIC CALCULATOR
        // =====================================

        stage('Upgrade to Scientific Calculator') {
            steps {
                echo "Switching to calc2.py for Build 2"

                bat """
                    copy /Y calc2.py calc.py
                """
            }
        }
        
        // =====================================
        // RESTORE ORIGINAL CALCULATOR
        // =====================================

        stage('Restore Original Calculator') {
            steps {
                echo "Restoring original calc.py"

                bat """
                    copy /Y calc_backup.py calc.py
                    del calc_backup.py
                """
            }
        }

        stage('Build 2 - Sanity Tests (Scientific Features)') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/sanity_test.py --junitxml=b2-sanity.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Build2 Sanity tests failed") }
                }
            }
        }

        stage('Build 2 - Slow Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/slow_test.py --junitxml=b2-slow.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Build2 Slow tests failed") }
                }
            }
        }

        stage('Build 2 - UI Tests') {
            steps {
                script {
                    def status = bat(
                        script: "python -m pytest tests/test_calc_ui.py --junitxml=b2-ui.xml",
                        returnStatus: true
                    )
                    if (status != 0) { unstable("Build2 UI tests failed") }
                }
            }
        }

        

        stage('Debug XML Results') {
            steps {
                bat "dir *.xml"
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: "*.xml"

            echo "======================================"
            echo "Final Build Status: ${currentBuild.currentResult}"
            echo "======================================"
        }
    }
}
