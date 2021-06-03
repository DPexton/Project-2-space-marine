pipeline {
        agent any
        environment {
            docker-credentials = credentials('docker-credentials')
            DATABASE_URI = credentials('DATABASE_URI')
        }
        stages{
            stage('Build Images'){
                steps{
                    sh "bash scripts/build.sh"
                }
            }
            stage('test'){
                steps{
                    sh "bash scripts/test.sh"
                }
            }
            stage('Deploy'){
                steps{
                    sh "bash scripts/deploy.sh"
                }
            }
        }
}