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
                'Smoke Tests': {
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

                'Slow Tests': {
                    steps {
                        bat '''
                        pytest -m slow ^
                        --junitxml=reports/slow.xml
                        '''
                    }
                }

                'Security Tests': {
                    steps {
                        bat '''
                        pytest -m security ^
                        --junitxml=reports/security.xml
                        '''
                    }
                }

                'UI Tests': {
                    steps {
                        bat '''
                        pytest tests/test_calc_ui.py ^
                        --junitxml=reports/ui.xml
                        '''
                    }
                }
            }
        }
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
                        pytest tests/test_calc_ui.py ^
                        --junitxml=reports/ui.xml
                        '''
                    }
                }
            }
        }
    }
}
