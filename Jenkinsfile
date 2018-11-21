pipeline {
    agent {dockerfile true}
    stages{
        stage("Tuildout"){
            steps{
                sh "buildout"
            }
        }
        stage("Test"){
            steps{
                sh "cd /usr/src/app && bin/test"
            }
        }
    }

}
