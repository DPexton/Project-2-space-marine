pipeline {
        agent any
        stages{
            stage('Build Images'){
                steps{
                    sh "./scripts/build.sh"
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