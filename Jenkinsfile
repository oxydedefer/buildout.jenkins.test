pipeline {
    agent {dockerfile true}
    stages{
        stage("clone"){
            steps{
                git "https://github.com/oxydedefer/buildout.jenkins.test.git"
            }
        }
    }

}