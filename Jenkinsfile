pipeline {
    agent any
stages {
    
   stage('Setup') {
            steps {
                // Set up your Python environment (e.g., virtualenv)
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
    
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Shivammdh/E-commerce-Hybrid-FW.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Shivammdh/E-commerce-Hybrid-FW.git'
                
            }
        }
        
        // stage('Setup') {
        //     steps {
        //         bat "python -m pip install -r requirements.txt" // Install necessary packages
        //     }
        // }
        
        stage('Run Selenium Script') {
            steps {
                sh "python -m Utilites.PassArgument" // Replace with the path to your script
            }
        }
    }
    
}
