pipeline {
        agent any
        environment {
            docker_credentials = credentials('docker_credentials')
            DATABASE_URI=credentials('DATABASE_URI')
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
            stage('config'){
                steps{
                    sh "bash asnsible.sh"
                    sh "ansible-playbook -i inventory.yaml playbook.yaml"
                }
            }
            stage('Deploy'){
                steps{
                    sh "bash scripts/deploy.sh"
                }
            }
        }
        post{
            always{
                junit "junit/*.xml"
                cobertura coberturaReportFile: 'coverage.xml', failNoReports:false
            }
        }
}