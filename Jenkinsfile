pipeline {
    agent any
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
                // Set up your Python environment (e.g., virtualenv)
                // def newEnv = ["PATH+=%SystemRoot%\\system32"]
                // bat(script: "set", returnStatus: true, env: newEnv)
                // bat 'python -m venv venv'
                // bat 'venv\\Scripts\\activate'
                bat "D:\\Windows\\cmd.exe /c pip install -r requirements.txt"
            }
        }
        
        
        // stage('Setup') {
        //     steps {
        //         bat "D:\\Windows\\cmd.exe /c python -m pip install -r requirements.txt" // Install necessary packages
        //     }
        // }
        
        stage('Run Selenium Script') {
            steps {
                bat "D:\\Windows\\cmd.exe /c python -m Utilites.PassArgument" // Replace with the path to your script
            }
        }
    }
    
}
