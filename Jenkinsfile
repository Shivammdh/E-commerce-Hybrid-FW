pipeline {
    agent any
    
    environment {
        PYTHON_HOME = "C:\\Users\\shivam.sharma\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" // Replace with your Python installation path
        PATH = "${env.PYTHON_HOME}\\Scripts;${env.PATH}"
    }
    
    stages {
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
        
        stage('Setup') {
            steps {
                bat "python -m pip install -r requirements.txt" // Install necessary packages
            }
        }
        
        stage('Run Selenium Script') {
            steps {
                bat "python -m Utilites.PassArgument" // Replace with the path to your script
            }
        }
    }
    
    // post {
    //     always {
    //         // You can add cleanup or notification steps here
    //     }
    // }
}
