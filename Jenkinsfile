pipeline {
        agent any
        environment {
            SECRET_KEY = credentials('SECRET_KEY')
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