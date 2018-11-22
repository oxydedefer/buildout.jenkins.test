pipeline {
    agent {dockerfile true}
    stages{
        stage("Buildout"){
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
    post {
      unstable {
         slackSend color: "warning", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was unstable"
      }
      success {
        slackSend color: "good", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was successful"
      }
      failure {
        slackSend color: "danger", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was failed"
      }
    }
}
