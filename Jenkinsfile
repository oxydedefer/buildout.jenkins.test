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
        always {
            steps{
                buildResult = currentBuild.currentResult
                if ( buildResult == "SUCCESS" ) {
                    slackSend color: "good", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was successful"
                  }
                  else if( buildResult == "FAILURE" ) {
                    slackSend color: "danger", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was failed"
                  }
                  else if( buildResult == "UNSTABLE" ) {
                    slackSend color: "warning", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was unstable"
                  }
                  else {
                    slackSend color: "danger", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} its resulat was unclear"
                  }

            }
        }
    }

}
