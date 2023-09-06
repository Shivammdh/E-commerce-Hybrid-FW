pipeline {
    agent any
stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Shivammdh/E-commerce-Hybrid-FW.git']]])
            }
        }
        stage('Setup') {
            steps {
                // Set up your Python environment (e.g., virtualenv)
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
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
                bat "python -m Utilites.PassArgument" // Replace with the path to your script
            }
        }
    }
    
}
