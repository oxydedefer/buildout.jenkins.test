pipeline {
    agent {dockerfile true}
    stages{
        stage("Tuildout"){
            steps{
                sh "cd /usr/src/app && bin/buildout"
            }
        }
        stage("Test"){
            steps{
                sh "cd /usr/src/app && bin/test"
            }
        }
    }

}
