pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest junitparser'
                sh 'mkdir -p reports'
            }
        }

        stage('Run Tests in Parallel') {
            parallel {
                stage('Smoke') {
                    steps {
                        sh 'pytest -m smoke --junitxml=reports/smoke.xml'
                    }
                }
                stage('Slow') {
                    steps {
                        sh 'pytest -m slow --junitxml=reports/slow.xml'
                    }
                }
                stage('Security') {
                    steps {
                        sh 'pytest -m security --junitxml=reports/security.xml'
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
                sh 'python dashboard.py'
            }
        }

        stage('Archive Dashboard') {
            steps {
                archiveArtifacts artifacts: 'dashboard/summary.html', fingerprint: true
            }
        }
    }
}
