pipeline {
        agent any
        environment{
            docker_hub_credentials = credentials('docker-hub-credentials')
        }
        stages{
            stage('Build Images'){
                steps{
                    sh "docker-compose build --parallel"  
                }
            }
            stage('test'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Deploy'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
}